# https://www.codeeval.com/open_challenges/40/

# Self Describing Numbers
# Challenge Description:

# A number is a self-describing number when (assuming digit positions are
# labeled 0 to N-1), the digit in each position is equal to the number of
# times that that digit appears in the number.
# Input sample:

# The first argument is the pathname to a file which contains test data,
# one test case per line. Each line contains a positive integer. E.g.

# 2020
# 22
# 1210

# Output sample:

# If the number is a self-describing number, print out 1. If not, print
# out 0. E.g.

# 1
# 0
# 1

# For the curious, here's how 2020 is a self-describing number: Position
# '0' has value 2 and there is two 0 in the number. Position '1' has
# value 0 because there are not 1's in the number. Position '2' has
# value 2 and there is two 2. And the position '3' has value 0 and
# there are zero 3's.

import sys


def check_if_sd_number(num):
    num_d = {}
    for n in [int(x) for x in num]:
        if n in num_d:
            num_d[n] += 1
        else:
            num_d[n] = 1
    for idx, n in enumerate(num):
        if idx in num_d:
            if num_d[idx] != int(n):
                return 0
        elif int(n) != 0:
            return 0
    return 1

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print check_if_sd_number(line.strip())
