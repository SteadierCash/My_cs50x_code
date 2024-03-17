from cs50 import get_int


while True:
    h = get_int("Height: ")
    if h > 0 and h < 9:
        break

for i in range(h):
    blank = h - i - 1
    hash = i + 1
    print(" " * blank + "#" * hash + "  " + "#" * hash)
