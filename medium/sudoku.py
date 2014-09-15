# https://www.codeeval.com/open_challenges/78/

# Sudoku
# Challenge Description:

# Sudoku is a number-based logic puzzle. It typically comprises of a 9*9
# grid with digits so that each column, each row and each of the nine 3*3
# sub-grids that compose the grid contains all the digits from 1 to 9.
# For this challenge, you will be given an N*N grid populated with numbers
# from 1 through N and you have to determine if it is a valid sudoku
# solution. You may assume that N will be either 4 or 9. The grid can be
# divided into square regions of equal size, where the size of a region
# is equal to the square root of a side of the entire grid. Thus for a 9*9
# grid there would be 9 regions of size 3*3 each.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains the value of N, a semicolon and the
# sqaure matrix of integers in row major form, comma delimited. E.g.

# 4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2
# 4;2,1,3,2,3,2,1,4,1,4,2,3,2,3,4,1

# Output sample:

# Print out True/False if the grid is a valid sudoku layout. E.g.

# True
# False

import sys
import math


def check_valid_sudoku_grid(n, grid):
    grid = [int(x) for x in grid.split(',')]
    n_set = set([x for x in range(1, int(n) + 1)])
    itvl = int(math.sqrt(int(n)))
    #check rows
    for i in range(0, len(grid), int(n)):
        if set(grid[i:(i + int(n))]) != n_set:
            return False
    #check columns
    for i in range(1, itvl):
        col = [x for idx, x in enumerate(grid) if not (idx + 1) % i]
        if set(col) != n_set:
            return False
    #check subgrids
    m_grid = []
    for i in range(0, len(grid), itvl):
        m_grid.append(grid[i:(i + itvl)])
    for i in range(0, len(m_grid), int(n)):
        for j in range(itvl):
            nidx = i + j
            grid_block = []
            for j in range(itvl):
                jidx = nidx + (itvl * j)
                grid_block.extend(m_grid[jidx])
            if set(grid_block) != n_set:
                return False
    return True

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print check_valid_sudoku_grid(*line.strip().split(";"))
