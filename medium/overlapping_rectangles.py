# https://www.codeeval.com/open_challenges/70/

# Overlapping Rectangles
# Challenge Description:

# Given two axis aligned rectangles A and B, determine if the two overlap.
# The rectangles considered overlapping if they have at least one common
# point.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains 8 comma separated co-ordinates. The
# co-ordinates are upper left x of A, upper left y of A, lower right x of
# A, lower right y of A, upper left x of B, upper left y of B, lower right
# x of B, lower right y of B. E.g.

# -3,3,-1,1,1,-1,3,-3
# -3,3,-1,1,-2,4,2,2

# Output sample:

# Print out True or False if A and B intersect.
# E.g.

# False
# True

import sys


def get_overlapping(coords):
    coords = [int(x) for x in coords]
    A = ((coords[0], coords[2]), (coords[1], coords[3]))
    B = ((coords[4], coords[6]), (coords[5], coords[7]))
    pairs = ((A, B), (B, A))
    for rect, comp in pairs:
        for point in rect[0]:
            if (comp[0][0] <= point <= comp[0][1]):
                for point in rect[1]:
                    if (comp[1][0] >= point >= comp[1][1]):
                        return True
    return False


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print get_overlapping(line.strip().split(","))
