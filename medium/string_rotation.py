# https://www.codeeval.com/open_challenges/76/

# String Rotation
# Challenge Description:

# You are given two strings. Determine if the second string is a rotation
# of the first string.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains two comma separated strings.
# E.g.

# Hello,lloHe
# Basefont,tBasefon

# Output sample:

# Print out True/False if the second string is a rotation of the first.
# E.g.

# True
# True

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        str1, str2 = line.strip().split(',')
        print str1 in str2 + str2
