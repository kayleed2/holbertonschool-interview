#include "slide_line.h"

/**
 * reverse_array - reverses an array in pointer
 *
 * @array: array pointer to revers
 * @size: size of array to reverse
 */
void reverse_array(int *array, size_t size)
{
	size_t old, new, temp;

	for (old = 0, new = size - 1; old < size / 2; old++, new --)
	{
		temp = array[old];
		array[old] = array[new];
		array[new] = temp;
	}
}

/**
 * slide_line - Slide and combine integers like 2048
 *
 * @line: pointer to int array of size @size
 * @size: size of int array
 * @direction: 1/0 to indicate SLIDE_LEFT or SLIDE_RIGHT
 *
 * Return: 1 upon success, or 0 upon failure
 */
int slide_line(int *line, size_t size, int direction)
{
	size_t one, two;

	if (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
		return (0);

	if (direction == SLIDE_RIGHT)
		reverse_array(line, size);

	for (one = 0, two = 0; one < size; one++)
		if (line[one] != 0)
			line[two++] = line[one];

	while (two < size)
		line[two++] = 0;


	for (one = 0; line[one] != 0; one++)
	{

		if (line[one] == line[one + 1])
		{
			line[one] *= 2;

			for (two = one + 1; two < size; two++)
				line[two] = two == size - 1 ? 0 : line[two + 1];
		}
	}

	if (direction == SLIDE_RIGHT)
		reverse_array(line, size);

	return (1);
}
