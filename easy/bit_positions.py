# https://www.codeeval.com/open_challenges/19/

# Bit Positions
# Challenge Description:

# Given a number n and two integers p1,p2 determine if the bits in position
# p1 and p2 are the same or not. Positions p1 and p2 are 1 based.
# Input sample:

# 86,2,3
# 125,1,2

# The first argument will be a path to a filename containing a comma
# separated list of 3 integers, one list per line. E.g.
# Output sample:

# Print to stdout, 'true'(lowercase) if the bits are the same, else
# 'false'(lowercase). E.g.

# true
# false

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        num, pos1, pos2 = line.strip().split(",")
        num = list(bin(int(num)))
        print num
        if num[-int(pos1)] == num[-int(pos2)]:
            print "true"
        else:
            print "false"
