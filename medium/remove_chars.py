# https://www.codeeval.com/open_challenges/13/

# Remove Characters
# Challenge Description:

# Write a program to remove specific characters from a string.
# Input sample:

# The first argument will be a path to a filename containing an input
# string followed by a comma and then the characters that need to be
# scrubbed. E.g.

# how are you, abc
# hello world, def

# Output sample:

# Print to stdout, the scrubbed strings, one per line. Trim out any
# leading/trailing whitespaces if they occur. E.g.

# how re you
# hllo worl

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        string, rems = line.split(",")
        rems = set(rems.strip())
        for char in rems:
            string = string.replace(char, "")
        print string
