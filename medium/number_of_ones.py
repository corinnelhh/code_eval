# https://www.codeeval.com/open_challenges/16/

# Number of Ones
# Challenge Description:

# Write a program to determine the number of 1 bits in the internal
# representation of a given integer.
# Input sample:

# The first argument will be a path to a filename containing an integer,
# one per line. E.g.

# 10
# 22
# 56

# Output sample:

# Print to stdout, the number of ones in the binary form of each number.
# E.g.

# 2
# 3
# 3

import sys

with open(sys.argv[1], 'r') as f:
    for num in f.readlines():
        num = bin(int(num.strip()))
        ones = 0
        for dig in num[2:]:
            if int(dig) == 1:
                ones += 1
        print ones
