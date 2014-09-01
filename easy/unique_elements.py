# https://www.codeeval.com/open_challenges/29/

# Unique Elements
# Challenge Description:

# You are given a sorted list of numbers with duplicates. Print out the
# sorted list with duplicates removed.
# Input sample:

# File containing a list of sorted integers, comma delimited, one per line.
# E.g.

# 1,1,1,2,2,3,3,4,4
# 2,3,4,5,5

# Output sample:

# Print out the sorted list with duplicates removed, one per line.
# E.g.

# 1,2,3,4
# 2,3,4,5

import sys


def get_unique_els(nums):
    uniques = set(el for el in nums)
    print ",".join(sorted(uniques, key=lambda x: int(x)))

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        get_unique_els(line.strip().split(","))
