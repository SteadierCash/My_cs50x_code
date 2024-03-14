#include <cs50.h>
#include <stdio.h>

int check_len(long number);
long power(int number, int pow);
bool check_sum(long number);

int main(void)
{
    long number = get_long("Number: ");

    int length = check_len(number);
    int first_two = number / (power(10, (length - 2)));
    int first = number / (power(10, (length - 1)));

    if ((length == 15) & (first_two == 34 || first_two == 37) & check_sum(number))
    {
        printf("AMEX\n");
    }

    else if ((length == 16) & (first_two >= 51 & first_two <= 55) & check_sum(number))
    {
        printf("MASTERCARD\n");
    }

    else if ((length == 16 || length == 13) & (first == 4) & check_sum(number))
    {
        printf("VISA\n");
    }

    else
    {
        printf("INVALID\n");
    }
}

long power(int number, int pow)
{
    long outcome = 1;
    for (int i = 0; i < pow; i++)
    {
        outcome *= number;
    }
    return outcome;
}

int check_len(long number)
{
    int length = 0;
    while (number != 0)
    {
        length++;
        number /= 10;
    }
    return length;
}

bool check_sum(long number)
{
    int sum = 0;
    while (number != 0)
    {
        sum += (number % 10);

        number /= 10;

        if (check_len(((number % 10) * 2)) == 2)
        {
            sum += ((number % 10) * 2) % 10;
            sum += ((number % 10) * 2) / 10;
        }
        else
        {
            sum += (number % 10) * 2;
        }

        number /= 10;
    }

    if (sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
