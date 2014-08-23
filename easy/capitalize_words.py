# https://www.codeeval.com/open_challenges/93/

# Capitalize Words
# Challenge Description:

# Write a program which capitalizes the first letter of each word in a
# sentence.
# Input sample:

# Hello world
# javaScript language
# a letter
# 1st thing

# Your program should accept as its first argument a path to a filename.
# Input example is the following
# Output sample:

# Hello World
# JavaScript Language
# A Letter
# 1st Thing

# Print capitalized words in the following way.

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        line = [word[0].upper() + word[1:] for word in line.split()]
        print " ".join(line)
