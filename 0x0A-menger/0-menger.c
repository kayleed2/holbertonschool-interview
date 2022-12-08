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
printf("%c\n", '#');
}
else if (level > 0)
{
for (col = 0; col < size; col++)
{
for (row = 0; row < size; row++)
{
printf("%c", (print(row, col)));
}
printf("\n");
}
}
}

/**
 * print - prints certain char
 *
 * @row: row
 * @col: col
 * Return: print
 */

char print(int row, int col)
{
while (row || col)
{
if (row % 3 == 1 && col % 3 == 1)
return (' ');
row /= 3;
col /= 3;
}
return ('#');
}
