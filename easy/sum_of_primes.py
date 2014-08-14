# https://www.codeeval.com/open_challenges/4/

# Sum of Primes
# Challenge Description:

# Write a program to determine the sum of the first 1000 prime numbers.
# Input sample:

# There is no input for this program.
# Output sample:

# Your program should print the sum on stdout, i.e.

# 3682913


def first_n_primes(n=1000):
    primes = []
    i = 2
    while True:
        is_prime = True
        for num in range(2, i - 1):
            if not i % num:
                is_prime = False
        if is_prime:
            primes.append(i)
        i += 1
        if len(primes) >= 1000:
            return sum(primes)


if __name__ == "__main__":
    print first_n_primes()
