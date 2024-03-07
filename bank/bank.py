a = input("Greeting: ")

b = a.strip().lower()[:5]

if b == "hello":
    print("$0", end="")

elif b[0] == "h":
    print("$20", end="")

else:
    print("$100", end="")
