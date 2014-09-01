# https://www.codeeval.com/open_challenges/24/

# Sum of Integers from File
# Challenge Description:

# Print out the sum of integers read from a file.
# Input sample:

# The first argument to the program will be a path to a filename
# containing a positive integer, one per line. E.g.

# 5
# 12

# Output sample:

# Print out the sum of all the integers read from the file. E.g.

# 17

import sys

with open(sys.argv[1], 'r') as f:
    total = 0
    for line in f.readlines():
        total += int(line.strip())
    print total
