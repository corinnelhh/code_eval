# https://www.codeeval.com/open_challenges/46/

# Prime Numbers
# Challenge Description:

# Print out the prime numbers less than a given number N. For bonus points
# your solution should run in N*(log(N)) time or better. You may assume
# that N is always a positive integer.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file is one test case. Each test case will contain an
# integer n < 4,294,967,295.
# E.g.

# 10
# 20
# 100

# Output sample:

# For each line of input, print out the prime numbers less than N, in
# ascending order, comma delimited. (There should not be any spaces
# between the comma and numbers) E.g.

# 2,3,5,7
# 2,3,5,7,11,13,17,19
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97


import sys
import math


def sieve_of_eratosthenes(nums, i):
    if i >= math.sqrt(nums[-1]):
        return nums
    nums = [num for num in nums if num % i or num <= i]
    return sieve_of_eratosthenes(nums, i + 1)


def get_primes(n):
    nums = [i for i in range(2, n)]
    primes = sieve_of_eratosthenes(nums, 2)
    print ",".join([str(num) for num in primes])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            get_primes(int(line.strip()))
