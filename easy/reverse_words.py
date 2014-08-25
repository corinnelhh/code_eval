# https://www.codeeval.com/open_challenges/8/

# Reverse words
# Challenge Description:

# Write a program to reverse the words of an input sentence.
# Input sample:

# The first argument will be a path to a filename containing multiple
# sentences, one per line. Possibly empty lines too. E.g.

# Hello World
# Hello CodeEval

# Output sample:

# Print to stdout, each line with its words reversed, one per line. Empty
# lines in the input should be ignored. Ensure that there are no trailing
# empty spaces on each line you print.
# E.g.

# World Hello
# CodeEval Hello

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print " ".join(line.strip().split()[::-1])
