#include <stdio.h>
#include <math.h>
#include <string.h>

#define TAB_SIZE 1760

int main()
{
    float A = 0;
    float B = 0;
    float i, j;
    float z[TAB_SIZE];
    char b[TAB_SIZE];

    printf("\x1b[2J");
    while (1)
    {   
        memset(b, 32, TAB_SIZE);
        memset(z, 0, TAB_SIZE * 4);

        for (j = 0; j < 6.28; j += 0.07)
            for (i = 0; i < 6.28; i += 0.02)
            {
                float c = sin(i);
                float d = cos(j);
                float e = sin(A);
                float f = sin(j);
                float g = cos(A);
                float h = d + 2;
                float D = 1./(c * h * e + f* g + 5);
                float l = cos(i);
                float m = cos(B);
                float n = sin(B);
                float t = c * h * g - f * e;
                int x = 40 + 30 * D * (l * h * m - t * n);
                int y = 12 + 15 * D * (l * h * n + t * m);
                int o = x + 80 * y;
                int N = 8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n);

                if (22 > y && y > 0 && x > 0 && 80 > x && D > z[o])
                {
                    z[o] = D;
                    b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
                }
            }
        
        printf("\x1b[H");

        for (int k = 0; k < TAB_SIZE; ++k)
            putchar(k % 80 ? b[k] : 10);
        
        A += 0.04;
        B += 0.02;
    }
    


    return 0;
}