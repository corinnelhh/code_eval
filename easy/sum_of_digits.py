# https://www.codeeval.com/open_challenges/21/

# Sum of Digits
# Challenge Description:

# Given a positive integer, find the sum of its constituent digits.
# Input sample:

# The first argument will be a path to a filename containing positive
# integers, one per line. E.g.

# 23
# 496

# Output sample:

# Print to stdout, the sum of the numbers that make up the integer, one
# per line. E.g.

# 5
# 19

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print sum([int(n) for n in line.strip()])
