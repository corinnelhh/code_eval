# https://www.codeeval.com/open_challenges/9/

# Stack Implementation
# Challenge Description:

# Write a program implementing a stack inteface for integers.The interface
# should have 'push' and 'pop' functions. You will be asked to 'push' a
# series of integers and then 'pop' and print out every alternate integer.
# Input sample:

# Your program should accept as its first argument a path to a filename
# containing a series of space delimited integers, one per line. E.g.

# 1 2 3 4
# 10 -2 3 4

# Output sample:

# Print to stdout, every alternate integer(space delimited), one per line.
# E.g.

# 4 2
# 4 -2

import sys

with open(sys.argv[1], 'r') as f:
    for num in f.readlines():
        print " ".join([str(i) for idx, i in enumerate(
            num.split()[::-1]) if not (idx + 2) % 2])
