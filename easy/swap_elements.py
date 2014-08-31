# https://www.codeeval.com/open_challenges/112/

# Swap Elements
# Challenge Description:

# You are given a list of numbers which is supplemented with positions
# that have to be swapped.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Input example is the following

# 1 2 3 4 5 6 7 8 9 : 0-8
# 1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

# As you can see a colon separates numbers with positions.
# Positions start with 0.
# You have to process positions left to right. In the example above
# (2nd line) first you process 0-1, then 1-3.
# Output sample:

# Print the lists in the following way.

# 9 2 3 4 5 6 7 8 1
# 2 4 3 1 5 6 7 8 9 10

import sys


def swap_els(nums, to_swap):
    nums = nums.split()
    to_swap = [el.strip().split("-") for el in to_swap.split(",")]
    for pair in to_swap:
        first, second = int(pair[0]), int(pair[1])
        nums[first], nums[second] = nums[second], nums[first]
    print " ".join(nums)

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        swap_els(*line.strip().split(":"))
