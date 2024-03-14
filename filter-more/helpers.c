#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float avg = (float) (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3;

            int roundedAvg = (int) (avg + 0.5);

            // Set each channel to the rounded average
            image[i][j].rgbtBlue = roundedAvg;
            image[i][j].rgbtGreen = roundedAvg;
            image[i][j].rgbtRed = roundedAvg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        RGBTRIPLE *new_row = malloc(width * sizeof(RGBTRIPLE) + 1);

        for (int j = 0; j < width; j++)
        {
            new_row[j] = image[i][width - j - 1];
        }

        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_row[j];
        }
        free(new_row);
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE(*new_image)[width] = malloc(height * sizeof(RGBTRIPLE[width]));

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red_sum = 0;
            float green_sum = 0;
            float blue_sum = 0;
            int counter = 0;

            for (int h = -1; h < 2; h++)
            {
                for (int w = -1; w < 2; w++)
                {
                    int new_i = i + h;
                    int new_j = j + w;

                    if (new_i >= 0 && new_i <= height - 1 && new_j >= 0 && new_j <= width - 1)
                    {
                        red_sum += image[new_i][new_j].rgbtRed;
                        green_sum += image[new_i][new_j].rgbtGreen;
                        blue_sum += image[new_i][new_j].rgbtBlue;
                        counter++;
                    }
                }
            }

            float avg_red = red_sum / counter;
            float avg_green = green_sum / counter;
            float avg_blue = blue_sum / counter;

            new_image[i][j].rgbtRed = (int) (avg_red + 0.5);
            new_image[i][j].rgbtGreen = (int) (avg_green + 0.5);
            new_image[i][j].rgbtBlue = (int) (avg_blue + 0.5);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }

    free(new_image);
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE(*new_image)[width] = malloc(height * sizeof(RGBTRIPLE[width]));

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red_sum_x = 0;
            int green_sum_x = 0;
            int blue_sum_x = 0;

            int red_sum_y = 0;
            int green_sum_y = 0;
            int blue_sum_y = 0;

            int g_x[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};

            int g_y[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

            for (int h = -1; h < 2; h++)
            {
                for (int w = -1; w < 2; w++)
                {
                    int new_i = i + h;
                    int new_j = j + w;

                    if (new_i >= 0 && new_i <= height - 1 && new_j >= 0 && new_j <= width - 1)
                    {
                        red_sum_x += image[new_i][new_j].rgbtRed * g_x[h + 1][w + 1];
                        green_sum_x += image[new_i][new_j].rgbtGreen * g_x[h + 1][w + 1];
                        blue_sum_x += image[new_i][new_j].rgbtBlue * g_x[h + 1][w + 1];

                        red_sum_y += image[new_i][new_j].rgbtRed * g_y[h + 1][w + 1];
                        green_sum_y += image[new_i][new_j].rgbtGreen * g_y[h + 1][w + 1];
                        blue_sum_y += image[new_i][new_j].rgbtBlue * g_y[h + 1][w + 1];
                    }
                }
            }

            float new_blue = sqrt(blue_sum_x * blue_sum_x + blue_sum_y * blue_sum_y);
            if (new_blue > 255)
            {
                new_blue = 255;
            }
            new_image[i][j].rgbtBlue = (int) (new_blue + 0.5);

            float new_green = sqrt(green_sum_x * green_sum_x + green_sum_y * green_sum_y);
            if (new_green > 255)
            {
                new_green = 255;
            }
            new_image[i][j].rgbtGreen = (int) (new_green + 0.5);

            float new_red = sqrt(red_sum_x * red_sum_x + red_sum_y * red_sum_y);
            if (new_red > 255)
            {
                new_red = 255;
            }
            new_image[i][j].rgbtRed = (float) (new_red + 0.5);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }

    free(new_image);
    return;
}
