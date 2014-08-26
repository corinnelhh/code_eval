# https://www.codeeval.com/open_challenges/81/

# Sum to Zero
# Challenge Description:

# You are given an array of integers. Count the numbers of ways in which
# the sum of 4 elements in this array results in zero.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file consist of comma separated positive and negative
# integers. E.g.

# 2,3,1,0,-4,-1
# 0,-1,3,-2

# Output sample:

# Print out the count of the different number of ways that 4 elements sum
# to zero. E.g.

# 2
# 1

import sys
import itertools


def get_count_zero_sums(line):
    nums = line.strip().split(",")
    count = 0
    combs = itertools.combinations(nums, 4)
    for comb in combs:
        sum_ = 0
        for num in comb:
            sum_ += int(num)
        if sum_ == 0:
            count += 1
    return count


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            print get_count_zero_sums(line)
