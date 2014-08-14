# https://www.codeeval.com/open_challenges/10/

# Mth to last element
# Challenge Description:

# Write a program to determine the Mth to last element of a list.
# Input sample:

# The first argument will be a path to a filename containing a series of
# space delimited characters followed by an integer representing a index
# into the list (1 based), one per line. E.g.

# a b c d 4
# e f g h 2

# Output sample:

# Print to stdout, the Mth element from the end of the list, one per line.
# If the index is larger than the list size, ignore that input. E.g.

# a
# g


import sys


def mth_to_last(line):
    line = line.split()
    num = int(line[-1]) + 1
    if num <= len(line):
        print line[- num]

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_:
        for line in input_.readlines():
            mth_to_last(line)
