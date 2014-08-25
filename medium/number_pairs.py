# https://www.codeeval.com/open_challenges/34/

# Number Pairs
# Challenge Description:

# You are given a sorted array of positive integers and a number 'X'.
# Print out all pairs of numbers whose sum is equal to X. Print out only
# unique pairs and the pairs should be in ascending order
# Input sample:

# Your program should accept as its first argument a filename. This file
# will contain a comma separated list of sorted numbers and then the sum
# 'X', separated by semicolon. Ignore all empty lines. If no pair exists,
# print the string NULL e.g.

# 1,2,3,4,6;5
# 2,4,5,6,9,11,15;20
# 1,2,3,4;50

# Output sample:

# Print out the pairs of numbers that equal to the sum X. The pairs should
# themselves be printed in sorted order i.e the first number of each pair
# should be in ascending order. E.g.

# 1,4;2,3
# 5,15;9,11
# NULL

import sys
import itertools


def get_sum_pairs(line):
    nums, target_sum = line.split(";")
    nums = nums.split(",")
    out = []
    combs = itertools.combinations(nums, 2)
    for nums in combs:
        num1, num2 = map(int, nums)
        if num1 + num2 == int(target_sum):
            pair = "{},{}".format(num1, num2)
            out.append(pair)
    if len(out):
        return ";".join(out)
    else:
        return "NULL"


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            print get_sum_pairs(line)
