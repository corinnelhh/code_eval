# https://www.codeeval.com/open_challenges/32/

# Trailing String
# Challenge Description:

# You are given two strings 'A' and 'B'. Print out a 1 if string 'B' occurs
# at the end of string 'A'. Else a zero.
# Input sample:

# The first argument will be the path to the input filename containing two
# strings, comma delimited, one per line. Ignore all empty lines in the
# input file. E.g.

# Hello World,World
# Hello CodeEval,CodeEval
# San Francisco,San Jose

# Output sample:

# Print out 1 if the second string occurs at the end of the first string.
# Else zero. Do NOT print out empty lines between your output. E.g.

# 1
# 1
# 0

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        str1, str2 = line.strip().split(",")
        if str1[::-1].startswith(str2[::-1]):
            print "1"
        else:
            print "0"
