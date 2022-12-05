#include "menger.h"

/**
 * menger - draws a 2D Menger Sponge
 *
 * @level: level of the Menger Sponge to draw
 */
void menger(int level)
{
    int row, col, size;

    size = pow(3, level);

    if (level == 0) 
    {
            printf("%c", '#');
    } else if (level > 0)
    {
        for (col = 0; col < size; col++)
        {
            for (row = 0; row < size; row++)
            {
                if ((col % 3 == 1) && (row % 3 == 1))
                    printf(" ");
                else
                    printf("%c", '#');
            // col /= 3;
		    // row /= 3;
            }
            printf("\n");
        }
    }
}