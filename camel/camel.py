a = input("camelCase: ")

a_low = a.lower()

snake = ""

for i in range(len(a)):
    if a[i] == a_low[i]:
        snake += a[i]

    else:
        snake += "_" + a[i].lower()

print(f"snake_case: {snake}")



