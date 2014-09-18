# https://www.codeeval.com/open_challenges/104/

# Word to Digit
# Challenge Description:

# Having a string representation of a set of numbers you need to print
# this numbers.

# All numbers are separated by semicolon. There are up to 20 numbers
# in one line. The numbers are "zero" to "nine"
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file is one test case. E.g.

# zero;two;five;seven;eight;four
# three;seven;eight;nine;two

# Output sample:

# Print numbers in the following way:

# 025784
# 37892

import sys


def get_digits(line):
    digits = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    print "".join([str(digits[n]) for n in line])

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        get_digits(line.strip().split(";"))
