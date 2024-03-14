// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, int tip);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// TODO: Complete the function
float half(float bill, float tax, int tip)
{
    // tax /= 100;
    // printf("%f", tax);
    // tip = (float) tip / 100.0;
    // printf("%f", tip);
    float total_bill = bill + bill * tax / 100.0 + bill * (float) tip / 100.0;

    return total_bill / 2;
}