#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    float index = (0.0588 * ((float) count_letters(text) / count_words(text) * 100)) -
                  (0.296 * ((float) count_sentences(text) / count_words(text) * 100)) - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        if ((int) index + 0.5 < index)
        {
            index++;
        }
        printf("Grade %i\n", (int) index);
    }
}

int count_letters(string text)
{
    int counter = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (tolower(text[i]) >= 'a' && tolower(text[i]) <= 'z')
        {
            counter++;
        }
    }
    return counter;
}

int count_words(string text)
{
    int counter = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            counter++;
        }
    }
    return counter;
}

int count_sentences(string text)
{
    int counter = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            counter++;
        }
    }
    return counter;
}
