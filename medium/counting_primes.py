# https://www.codeeval.com/open_challenges/63/

# Counting Primes
# Challenge Description:

# Given two integers N and M, count the number of prime numbers between N
# and M (both inclusive)
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains two comma separated positive integers.
# E.g.

# 2,10
# 20,30

# Output sample:

# Print out the number of primes between N and M (both inclusive)

# 4
# 2

import sys
import math


def sieve_of_eratosthenes(nums, i):
    if i > math.sqrt(nums[-1]):
        return nums
    nums = [num for num in nums if num % i or num <= i]
    return sieve_of_eratosthenes(nums, i + 1)


def get_primes_count(line):
    num1, num2 = line.strip().split(",")
    num_set = [i for i in range(int(num1), int(num2) + 1)]
    if len(num_set):
        return len(sieve_of_eratosthenes(num_set, 2))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            print get_primes_count(line)
