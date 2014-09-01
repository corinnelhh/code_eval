# https://www.codeeval.com/open_challenges/38/

# String List
# Challenge Description:

# Credits: Challenge contributed by Max Demian.

# You are given a number N and a string S. Print all of the possible ways
# to write a string of length N from the characters in string S, comma
# delimited in alphabetical order.
# Input sample:

# The first argument will be the path to the input filename containing
# the test data. Each line in this file is a separate test case. Each
# line is in the format: N,S i.e. a positive integer, followed by a
# string (comma separated). E.g.

# 1,aa
# 2,ab
# 3,pop

# Output sample:

# Print all of the possible ways to write a string of length N from the
# characters in string S comma delimited in alphabetical order, with
# no duplicates. E.g.

# a
# aa,ab,ba,bb
# ooo,oop,opo,opp,poo,pop,ppo,ppp

import sys
import itertools


def get_perms(lim, chars):
    chars = [char for char in set(chars) for i in range(int(lim))]
    perms = itertools.permutations(chars, int(lim))
    print ",".join(sorted("".join(perm) for perm in set(perms)))

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        get_perms(*line.strip().split(','))
