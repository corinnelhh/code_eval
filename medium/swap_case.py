# https://www.codeeval.com/open_challenges/96/

# Swap Case
# Challenge Description:

# Write a program which swaps letters' case in a sentence. All non-letter
# characters should remain the same.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Input example is the following

# Hello world!
# JavaScript language 1.8
# A letter

# Output sample:

# Print results in the following way.

# hELLO WORLD!
# jAVAsCRIPT LANGUAGE 1.8
# a LETTER

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print "".join([ch.upper() if ch == ch.lower() else ch.lower()
                      for w in line.strip() for ch in w])


    # for line in f.readlines():
    #     print "".join(["".join([ch.upper() if ch == ch.lower() else ch.lower()
    #                             for ch in w]) for w in line.strip()])
