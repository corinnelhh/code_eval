# https://www.codeeval.com/open_challenges/99/

# Calculate Distance
# Challenge Description:

# You have coordinates of 2 points and need to find the distance between them.
# Input sample:


# Your program should accept as its first argument a path to a filename.
# Input example is the following


# (25, 4) (1, -6)
# (47, 43) (-25, -11)

# All numbers in input are integers between -100 and 100.
# Output sample:

# Print results in the following way.

# 26
# 90

# You don't need to round the results you receive.
# They must be integer numbers between -100 and 100.

import sys
import math


def get_distance(line):
    p_s = [[int(i.strip()) for i in el.split(",")] for el in line[1:-1].split(") (")]
    x_dif, y_dif = (p_s[0][0] - p_s[1][0]), (p_s[0][1] - p_s[1][1])
    print int(math.sqrt((x_dif ** 2) + (y_dif ** 2)))

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        get_distance(line.strip())
