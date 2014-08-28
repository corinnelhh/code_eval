# https://www.codeeval.com/open_challenges/153/

# Locks
# Challenge Description:

# There are "n" unlocked rooms located in a row along a long corridor.

# A security guard starts at the beginning of the corridor, passes by and
# locks the lock of every second door(2, 4, 6 ...). If a lock was open,
# it now becomes closed, if it was closed, it stays closed. He then
# returns to the beginning of the corridor and switches the lock to the
# opposite position on every third door(3, 6, 9 ...): if the door's lock
# was open before, he close it and vice versa. This algorithm (first every
# second door's lock is closed; then every third door's lock is switched
# to the opposite position) repeats "m"-1 times.

# On his last pass (the "m" one), only the last door's lock must be
# switched without any additional actions.

# Your job is to determine how many doors have been left unlocked.

# Input sample:

# 3 1
# 100 100

# Your program should accept as its first argument a path to a filename.

# Each line of input contains 2 integer - n - number of locks and m - how
# many times to repeat actions:

# Output sample:

# For each line of input print out how many door are left unlocked:

# 2
# 50

import sys


def get_unlocked_doors(locks, passes):
    locks_dict = {i: False for i in range(locks)}
    for i in range(passes - 1):
        for i in range(locks):
            if not (i + 1) % 2:
                locks_dict[i] = True
        for i in range(locks):
            if not (i + 1) % 3:
                locks_dict[i] = not locks_dict[i]
    locks_dict[locks - 1] = not locks_dict[locks - 1]
    print len([k for k, v in locks_dict.items() if not v])


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        get_unlocked_doors(*(int(n) for n in line.strip().split()))
