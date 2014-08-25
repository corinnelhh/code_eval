# https://www.codeeval.com/open_challenges/22/

# Fibonacci Series
# Challenge Description:

# The Fibonacci series is defined as:
# F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1.
# Given a positive integer 'n', print out the F(n).
# Input sample:

# The first argument will be a path to a filename containing a positive
# integer, one per line. E.g.

# 5
# 12

# Output sample:

# Print to stdout, the fibonacci number, F(n). E.g.

# 5
# 144

import sys


def fib_seq(num):
    if num <= 1:
        return num
    else:
        count, fib_num, old_fib = 1, 1, 0
        while count < num:
            count, fib_num, old_fib = count + 1, fib_num + old_fib, fib_num
        return fib_num

with open(sys.argv[1], 'r') as f:
    for num in f.readlines():
        print fib_seq(int(num.strip()))

