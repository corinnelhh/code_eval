# https://www.codeeval.com/open_challenges/15/

# Endianness
# Challenge Description:

# Write a program to print out the endianness of the system.
# Input sample:

# None
# Output sample:

# Print to stdout, the endianness, wheather it is LittleEndian or BigEndian.
# e.g.

# BigEndian

import sys

print {'little': 'LittleEndian', "big": 'BigEndian'}[sys.byteorder]
