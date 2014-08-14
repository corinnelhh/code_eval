# https://www.codeeval.com/open_challenges/2/

# Longest Lines
# Challenge Description:

# Write a program to read a multiple line text file and write the 'N'
# longest lines to stdout. Where the file to be read is specified on the
# command line.
# Input sample:

# 2
# Hello World
# CodeEval
# Quick Fox
# A
# San Francisco

# Your program should read an input file (the first argument to your program
#     will be a path to a filename). The first line contains the value of
# the number 'N' followed by multiple lines. You may assume that the input
# file is formatted correctly and the number on the first line i.e. 'N' is
# a valid positive integer. E.g.
# Output sample:

# The 'N' longest lines, newline delimited. Ignore all empty lines in the
# input. Ensure that there are no trailing empty spaces on each line you
# print. Also ensure that the lines are printed out in decreasing order of
# length i.e. the output should be sorted based on their length. E.g.

# San Francisco
# Hello World


import sys


def print_lines(lines):
    n = int(lines[0])
    lines = lines[1:]
    lines.sort(key=len)
    count = 0
    for line in lines[::-1]:
        count += 1
        print line
        if count >= n:
            break


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

        print_lines(lines)
