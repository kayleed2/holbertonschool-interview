#include "sandpiles.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * sandpiles_sum - computes the sum of two sandpiles
 *
 * @grid1: first grid
 * @grid2: second grid
 *
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
    print_grid(grid1);
    print_grid(grid2);
}

/**
 * print_grid - Print 3x3 grid
 *
 * @grid: 3x3 grid
 *
 */
void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}
