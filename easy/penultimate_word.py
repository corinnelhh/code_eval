# https://www.codeeval.com/open_challenges/92/

# Penultimate Word
# Challenge Description:

# Write a program which finds the next-to-last word in a string.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Input example is the following

# some line with text
# another line

# Each line has more than one word.
# Output sample:

# Print the next-to-last word in the following way.

# with
# another

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print line.strip().split()[-2]
