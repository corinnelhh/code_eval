# https://www.codeeval.com/open_challenges/18/

# Multiples of a Number
# Challenge Description:

# Given numbers x and n, where n is a power of 2, print out the smallest
# multiple of n which is greater than or equal to x. Do not use division
# or modulo operator.
# Input sample:

# The first argument will be a path to a filename containing a comma
# separated list of two integers, one list per line. E.g.

# 13,8
# 17,16

# Output sample:

# Print to stdout, the smallest multiple of n which is greater than or
# equal to x, one per line. E.g.

# 16
# 32

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        x, n = line.strip().split(",")
        total = 0
        while total < int(x):
            total += int(n)
        print total
