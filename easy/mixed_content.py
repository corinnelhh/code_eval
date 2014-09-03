# https://www.codeeval.com/open_challenges/115/

# Mixed Content
# Challenge Description:

# You have a string of words and digits divided by comma. Write a program
# which separates words with digits. You shouldn't change the order
# elements.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Input example is the following

# 8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21
# 24,13,14,43,41

# Output sample:

# melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21
# 24,13,14,43,41

# As you cas see you need to output the same input string if it has words
# only or digits only.

import sys


def separate_types(inp):
    nums, strings = [], []
    for i in inp:
        try:
            j = int(i)
            nums.append(i)
        except ValueError:
            strings.append(i)
    nums, strings = ",".join(nums), ",".join(strings)
    if len(nums):
        if len(strings):
            print "|".join([strings, nums])
        else:
            print nums
    else:
        print strings

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        separate_types(line.strip().split(','))
