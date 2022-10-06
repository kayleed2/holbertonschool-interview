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
int col, row;

	for (row = 0; row < 3; row++)
	{
		for (col = 0; col < 3; col++)
		{
			grid1[row][col] += grid2[row][col];
		}
	}
}
