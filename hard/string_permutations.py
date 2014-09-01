# https://www.codeeval.com/open_challenges/14/

# String Permutations
# Challenge Description:

# Write a program to print out all the permutations of a string in
# alphabetical order. We consider that
# digits < upper case letters < lower case letters. The sorting should be
# performed in ascending order.
# Input sample:

# Your program should accept as its first argument a path to a file
# containing an input string, one per line.
# E.g.

# hat
# abc
# Zu6

# Output sample:

# Print to stdout, permutations of the string, comma separated, in
# alphabetical order.
# E.g.

# aht,ath,hat,hta,tah,tha
# abc,acb,bac,bca,cab,cba
# 6Zu,6uZ,Z6u,Zu6,u6Z,uZ6

import sys
import itertools


def get_permutations(string):
    perms = itertools.permutations(string)
    print ",".join(sorted("".join(perm) for perm in perms))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            get_permutations(line.strip())
