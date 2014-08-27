# https://www.codeeval.com/open_challenges/3/

# Write a program to determine the biggest prime palindrome under 1000.
# Input sample:

# There is no input for this program.
# Output sample:

# Your program should print the largest palindrome on stdout, i.e.

# 929

import math


def prime_palindromes(n):
    nums = [i for i in range(2, n + 1)]
    primes = sieve_of_eratosthenes(nums, 2)
    for num in primes[::-1]:
        if str(num) == str(num)[::-1]:
            return num


def sieve_of_eratosthenes(nums, i):
    if i >= math.sqrt(nums[-1]):
        return nums
    nums = [num for num in nums if num % i or num <= i]
    return sieve_of_eratosthenes(nums, i + 1)


if __name__ == "__main__":
    print prime_palindromes(n=1000)
