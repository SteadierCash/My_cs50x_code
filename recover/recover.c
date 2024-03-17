#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int counter = 0;
    int first = 1;

    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("could not open the file");
        return 1;
    }

    uint8_t buffer[512];

    char *filename = malloc(8);
    sprintf(filename, "%03i.jpg", counter);
    FILE *new_file = fopen(filename, "w");

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (first == 1)
            {
                first++;
            }
            else if (first != 1)
            {
                fclose(new_file);
                counter++;
                sprintf(filename, "%03i.jpg", counter);
                new_file = fopen(filename, "w");
            }

            fwrite(buffer, 1, 512, new_file);
        }
        else
        {
            if (first != 1)
            {
                fwrite(buffer, 1, 512, new_file);
            }
        }
    }
    fclose(card);
    fclose(new_file);
    free(filename);
}
