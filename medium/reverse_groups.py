# https://www.codeeval.com/open_challenges/71/

# Reverse Groups
# Challenge Description:

# Given a list of numbers and a positive integer k, reverse the elements
# of the list, k items at a time. If the number of elements is not a
# multiple of k, then the remaining items in the end should be left as is.
# Input sample:

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains a list of numbers and the number k,
# separated by a semicolon. The list of numbers are comma delimited.
# E.g.

# 1,2,3,4,5;2
# 1,2,3,4,5;3

# Output sample:

# Print out the new comma separated list of numbers obtained after
# reversing. E.g.

# 2,1,4,3,5
# 3,2,1,4,5


# def reverse_chunks(line):
#     line, k = line.strip().split(";")
#     line, k = line.split(","), int(k)
#     if k == 1:
#         return ",".join(line)
#     out = []
#     last = 0
#     for i in range(k, len(line), k):
#         for j in line[last:i][::-1]:
#             out.append(j)
#         last = i
#     for i in range(-(len(line) % k), 0):
#         out.append(line[i])
#     return ",".join(out)


import sys


def reverse_chunks(line):
    line, k = line.strip().split(";")
    line, k = line.split(","), int(k)
    for j in range(0, (len(line) - len(line) % k), k):
        line[j: j + k] = line[j: j + k][::-1]
    return ",".join(line)


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print reverse_chunks(line)
