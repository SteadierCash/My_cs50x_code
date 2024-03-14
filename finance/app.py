import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    data = db.execute("SELECT s1.symbol, price, volume FROM\
                      (SELECT symbol, sum(volume) volume FROM stock s1 WHERE s1.user_id = ? GROUP BY symbol) s1\
                       LEFT JOIN (SELECT symbol, AVG(price) price FROM stock s1 WHERE s1.user_id = ? and volume > 0 GROUP BY symbol) s2 ON s1.symbol = s2.symbol",
                      session["user_id"], session["user_id"])

    stock_sum = 0

    for i in data:
        i["value"] = i["price"] * i["volume"]
        stock_sum += i["value"]
        i["value"] = usd(i["value"])
        i["price"] = usd(i["price"])

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

    total = cash[0]["cash"] + stock_sum

    return render_template("index.html", data=data, cash=usd(cash[0]["cash"]), total=usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        stock = request.form.get("symbol")
        volume = request.form.get("shares")

        if not stock or not volume:
            return apology("must provide stock symbol and volume", 400)

        try:
            volume = int(volume)
        except ValueError:
            return apology("wrong volume format")

        if volume < 1:
            return apology("wrong volume format")

        data = lookup(stock.lower())

        if not data:
            return apology("Not a valid symbol", 400)

        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        current_cash = current_cash[0]["cash"]

        if (volume * int(data["price"])) > current_cash:
            return apology("Not enaugh cash", 400)

        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash - volume * data["price"], session["user_id"])

        db.execute("INSERT INTO stock (user_id, symbol, price, volume) VALUES(?, ?, ?, ?)",
                   session["user_id"], stock, data["price"], volume)
        db.execute("INSERT INTO all_stock (user_id, symbol, price, volume) VALUES(?, ?, ?, ?)",
                   session["user_id"], stock, data["price"], volume)
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    data = db.execute("SELECT * FROM stock WHERE user_id = ?", session["user_id"])

    for i in data:
        i["price"] = usd(i["price"])

    return render_template("history.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stock = request.form.get("symbol")
        if not stock:
            return apology("must provide stock symbol", 400)
        data = lookup(stock.lower())

        if not data:
            return apology("Not a valid symbol", 400)

        return render_template("quoted.html", symbol=data["symbol"], price=usd(data["price"]))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")

        if not name:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif password != confirm_password:
            return apology("confiramtion password must be the same", 400)
        elif db.execute("SELECT * FROM users WHERE username = ?", name):
            return apology("username is taken", 400)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, generate_password_hash(password))

        #  session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        stock = request.form.get("symbol")
        volume = request.form.get("shares")

        if not stock or not volume:
            return apology("must provide stock symbol and volume", 400)

        try:
            volume = int(volume)
        except ValueError:
            return apology("wrong volume format")

        data = lookup(stock.lower())

        if not data:
            return apology("Not a valid symbol", 400)

        current_volume = db.execute(
            "SELECT sum(volume) volume FROM stock WHERE user_id = ? and symbol = ? group by symbol", session["user_id"], stock)

        if current_volume == []:
            return apology("You don't have this stock", 400)

        current_volume = current_volume[0]["volume"]

        if volume > current_volume:
            return apology("You don't have so much volume")

        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        current_cash = current_cash[0]["cash"]

        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash + volume * data["price"], session["user_id"])

        db.execute("INSERT INTO stock (user_id, symbol, price, volume) VALUES(?, ?, ?, ?)",
                   session["user_id"], stock, data["price"], volume * -1)

        return redirect("/")
    else:
        stock = db.execute(
            "SELECT DISTINCT symbol, volume FROM stock WHERE user_id=? GROUP BY symbol HAVING volume > 0", session["user_id"])
        print(stock)
        return render_template("sell.html", stocks=stock)
