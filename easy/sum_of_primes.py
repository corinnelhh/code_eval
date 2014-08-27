# https://www.codeeval.com/open_challenges/4/

# Sum of Primes
# Challenge Description:

# Write a program to determine the sum of the first 1000 prime numbers.
# Input sample:

# There is no input for this program.
# Output sample:

# Your program should print the sum on stdout, i.e.

# 3682913


# def first_n_primes(n=1000):
#     primes = []
#     i = 2
#     while True:
#         is_prime = True
#         for num in range(2, i - 1):
#             if not i % num:
#                 is_prime = False
#         if is_prime:
#             primes.append(i)
#         i += 1
#         if len(primes) >= 1000:
#             return sum(primes)
import math


def sieve_of_eratosthenes(nums, i):
    if i >= math.sqrt(nums[-1]):
        return nums
    nums = [num for num in nums if num % i or num <= i]
    return sieve_of_eratosthenes(nums, i + 1)


def first_n_primes(n=8000):
    nums = [i for i in range(2, n + 1)]
    primes = sieve_of_eratosthenes(nums, 2)
    return sum(primes[:1000])


if __name__ == "__main__":
    print first_n_primes()
