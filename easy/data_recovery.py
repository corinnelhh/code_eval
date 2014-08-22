# https://www.codeeval.com/open_challenges/140/

# Data Recovery
# Challenge Description:

# Your friends decided to make a fun of you. They've installed a script to
# your computer which shuffled all of the words within a text. It was a
# joke, so they've left hints for each sentence which allow you to easily
# rebuild your data. The challenge is to write a program which reconstructs
# each sentence out of a set of words, you need to find out how to use a
# given hint and print out the original sentences.
# Input sample:

# 2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2
# programming first The language;3 2 1
# programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9

# Your program should accept as its first argument a path to a filename.
# Each line is a test case. Each test case consists of a set of words and
# a sequence of numbers separated by a semicolon. The words within a set
# and the numbers within a sequence are separated by a single whitespace.
# E.g.
# Output sample:

# However, it was not implemented until 1998 and 2000
# The first programming language
# The Manchester Mark 1 ran programs written in Autocode from 1952

# For each test case print out the reconstructed sentence one per line. E.g.

# Constraints:
# The number of test cases is in range [20, 40].
# The words consist of ASCII upper and lower case letters, digits and punctuation.

import sys


def get_original_sentence(line):
    text, nums = line.strip().split(";")
    text, nums = text.split(), map(int, nums.split())
    if len(text) - len(nums):
        for i in range(len(text)):
            if i + 1 not in nums:
                nums.append(i + 1)
    zipped = zip(tuple(text), tuple(nums))
    zipped.sort(key=lambda x: x[1])
    out = [i[0] for i in zipped]
    return " ".join(out)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            print get_original_sentence(line)
