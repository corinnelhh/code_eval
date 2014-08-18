# https://www.codeeval.com/open_challenges/62/

# N Mod M
# Challenge Description:

# Given two integers N and M, calculate N Mod M (without using any inbuilt
#     modulus operator).
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains two comma separated positive integers.
# E.g.

# 20,6
# 2,3

# You may assume M will never be zero.
# Output sample:

# Print out the value of N Mod M


import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        num1, num2 = line.split(",")
        mults = 0
        while mults <= int(num1) - int(num2):
            mults += int(num2)
        rem = int(num1) - mults
        print rem
