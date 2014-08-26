# https://www.codeeval.com/open_challenges/100/

# Even Numbers
# Challenge Description:

# Write a program which checks input numbers and determines whether a
# number is even or not.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Input example is the following

# 701
# 4123
# 2936

# Output sample:

# Print 1 if the number is even or 0 if the number is odd.

# 0
# 0
# 1

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if int(line.strip()) % 2:
            print 0
        else:
            print 1
