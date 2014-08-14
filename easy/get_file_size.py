#https://www.codeeval.com/open_challenges/26/
# Print the size of a file in bytes.
# Input:

# The first argument to your program has the path to the file you need to
# check the size of.
# Output sample:

# Print the size of the file in bytes. E.g.

# 55


import os
import sys


def get_file_size(f):
    stats = os.stat(f)
    print stats.st_size


if __name__ == "__main__":
    f = sys.argv[1]
    print get_file_size(f)
