# https://www.codeeval.com/open_challenges/12/

# First Non-Repeated Character
# Challenge Description:

# Write a program to find the first non repeated character in a string.
# Input sample:

# The first argument will be a path to a filename containing strings. E.g.

# yellow
# tooth

# Output sample:

# Print to stdout, the first non repeating character, one per line. E.g.

# y
# h


import sys
from collections import OrderedDict


def find_non_repeated(line):
    letters = OrderedDict({})
    for letter in line:
        if letter in letters:
            letters[letter] = True
        else:
            letters[letter] = False
    for key, val in letters.items():
        if not val:
            return key


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for line in lines:
        print find_non_repeated(line)
