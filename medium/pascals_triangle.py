# https://www.codeeval.com/open_challenges/66/

# Pascals Triangle
# Challenge Description:

# A Pascals triangle row is constructed by looking at the previous row
# and adding the numbers to its left and right to arrive at the new value.
# If either the number to its left/right is not present, substitute a
# zero in its place. More details can be found here: Pascal's triangle.
# E.g. a Pascal's triangle upto a depth of 6 can be shown as:

#             1
#           1   1
#         1   2   1
#        1  3   3   1
#      1  4   6   4   1
#     1  5  10  10  5   1

# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains a positive integer which indicates the
# depth of the triangle (1 based). E.g.

# 6

# Output sample:

# Print out the resulting pascal triangle upto the requested depth in
# row major form. E.g.

# 1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1

import sys
import itertools


def pascals_triangle(depth):
    row_count = 1
    rows = [[1]]
    while row_count < depth:
        new_row, last_el = [], 0
        for el in rows[-1]:
            new_row.append(last_el + el)
            last_el = el
        new_row.append(1)
        rows.append(new_row)
        row_count += 1
    return " ".join([str(n) for n in list(
        itertools.chain.from_iterable(rows))])


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print pascals_triangle(int(line.strip()))
