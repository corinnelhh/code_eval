# https://www.codeeval.com/open_challenges/47/

# Palindromic Ranges
# Challenge Description:

# A positive integer is a palindrome if its decimal representation (without
# leading zeros) is a palindromic string (a string that reads the same
# forwards and backwards). For example, the numbers 5, 77, 363, 4884, 11111,
# 12121 and 349943 are palindromes.

# A range of integers is interesting if it contains an even number of
# palindromes. The range [L, R], with L <= R, is defined as the sequence
# of integers from L to R (inclusive): (L, L+1, L+2, ..., R-1, R). L and R
# are the range's first and last numbers.

# The range [L1,R1] is a subrange of [L,R] if L <= L1 <= R1 <= R. Your job
# is to determine how many interesting subranges of [L,R] there are.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file is one test case. Each test case will contain two
# positive integers, L and R (in that order), separated by a space. eg.

# 1 2
# 1 7
# 87 88

# Output sample:

# For each line of input, print out the number of interesting subranges of
# [L,R] eg.

# 1
# 12
# 1

# For the curious: In the third example, the subranges are: [87]
# (0 palindromes), [87,88](1 palindrome),[88](1 palindrome).
# Hence the number of interesting palindromic ranges is 1.

import sys


def print_pal_ranges_of_interest(line):
    first, last = line.split()
    first, last = int(first), int(last) + 1
    interesting_ranges = 0
    for i in range(first, last):
        for j in range(i, last):
            pals = 0
            for k in range(i, j + 1):
                if str(k) == str(k)[::-1]:
                    pals += 1
            if not pals % 2:
                interesting_ranges += 1
    print interesting_ranges


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            print_pal_ranges_of_interest(line)


