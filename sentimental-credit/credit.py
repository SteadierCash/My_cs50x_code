from cs50 import get_int


def main():
    number = get_int("Number: ")
    length = len(str(number))
    # print(length)
    first_two = number // (10 ** (length - 2))
    # print(first_two)
    first = number // (10 ** (length - 1))
    # print(first)

    # print(check_sum(number))
    # print(length == 15 and (first_two == 34 or first_two == 37) and check_sum(number))

    if length == 15 and (first_two == 34 or first_two == 37) and check_sum(number):
        print("AMEX")

    elif length == 16 and (first_two >= 51 and first_two <= 55) and check_sum(number):
        print("MASTERCARD")

    elif (length == 16 or length == 13) and first == 4 and check_sum(number):
        print("VISA")

    else:
        print("INVALID")


def check_sum(number):
    sum = 0

    while number != 0:
        sum += number % 10

        number = number // 10

        if len(str((number % 10) * 2)) == 2:
            sum += ((number % 10) * 2) % 10
            sum += ((number % 10) * 2) // 10

        else:
            sum += (number % 10) * 2

        number //= 10

    if sum % 10 == 0:
        return True

    else:
        return False


main()
