from cs50 import get_string


def main():
    text = get_string("Text: ")

    index = (0.0588 * count_letters(text) / count_words(text) * 100) - \
        (0.296 * count_sentences(text) / count_words(text)) * 100 - 15.8

    if index < 1:
        print("Before Grade 1")

    elif index > 16:
        print("Grade 16+")

    else:
        print(index)
        print(f"Grade {round(index)}")


def count_letters(text):
    sum = 0

    for letter in text:
        if letter.lower() >= "a" and letter.lower() <= "z":
            sum += 1

    return sum


def count_words(text):
    sum = 1
    for letter in text:
        if letter == " ":
            sum += 1
    return sum


def count_sentences(text):
    sum = 0
    for letter in text:
        if letter in [".", "?", "!"]:
            sum += 1

    return sum


main()
