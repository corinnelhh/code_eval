# https://www.codeeval.com/open_challenges/111/

# Longest Word
# Challenge Description:

# In this challenge you need to find the longest word in a sentence. If
# the sentence has more than one word of the same length you should pick
# the first one.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Input example is the following

# some line with text
# another line

# Each line has one or more words. Each word is separated by space char.
# Output sample:

# Print the longest word in the following way.

# some
# another

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print max(line.strip().split(), key=len)
