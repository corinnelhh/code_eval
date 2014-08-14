#https://www.codeeval.com/open_challenges/26/
import os
import sys


def get_file_size(f):
    stats = os.stat(f)
    print stats.st_size


if __name__ == "__main__":
    f = sys.argv[1]
    print get_file_size(f)
