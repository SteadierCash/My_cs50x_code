a = [5, 10, 25]

due = 50
in_mach = 0

while True:
    b = int(input("Insert Coin:"))

    if b not in a:
        print(f"Amount Due: {due - in_mach}")
    elif due <= in_mach + b:
        print(f"Change Owed: {in_mach + b - due}")
        break
    else:
        in_mach += b
        print(f"Amount Due: {due - in_mach}")


