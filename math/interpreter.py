a = input("Expression: ")

b = a.split(" ")

b[0] = int(b[0])
b[2] = int(b[2])

match b[1]:
    case "+":
        print(float(b[0] + b[2]))

    case "-":
        print(float(b[0] - b[2]))

    case "/":
        if b[2] != 0:
            print(float(b[0] / b[2]))

        else:
            print("error")

    case "*":
        print(float(b[0] * b[2]))
