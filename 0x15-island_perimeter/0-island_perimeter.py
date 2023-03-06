#!/usr/bin/python3
"""Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """Function that return perimeter of island"""
    # define the height and width of the grid
    height, width = len(grid), len(grid[0])
    
    # initialize the perimeter to zero
    perimeter = 0
    
    # iterate through each cell in the grid
    for i in range(height):
        for j in range(width):
            # if the cell is land, add its perimeter to the total perimeter
            if grid[i][j] == 1:
                perimeter += 4
                
                # check the adjacent cells and reduce the perimeter accordingly
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
                    
    return perimeter
