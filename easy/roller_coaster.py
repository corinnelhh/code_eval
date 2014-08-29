# https://www.codeeval.com/open_challenges/156/

# Roller Coaster
# Challenge Description:

# You are given a text. Your job is to write a program to set the case of
# text characters based on the following:

#     First letter of the line should be upper case.
#     Next letter should be lower case.
#     Next letter should be upper case and so on...
#     Any characters, except the letters, are ignored during determination
#     of letters case.

# Input sample:

# The first argument will be a path to a filename containing sentences,
# one per line. You can assume all characters are from the english
# language. E.g.:

# To be, or not to be: that is the question.
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune,
# Or to take arms against a sea of troubles,
# And by opposing end them? To die: to sleep.

# Output sample:

# Print to stdout, the RoLlErCoAsTeR case version of the string. E.g.:

# To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.
# WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR
# ThE sLiNgS aNd ArRoWs Of OuTrAgEoUs FoRtUnE,
# Or To TaKe ArMs AgAiNsT a SeA oF tRoUbLeS,
# AnD bY oPpOsInG eNd ThEm? To DiE: tO sLeEp.

import sys


def roller_coaster(line):
    upper = True
    out = []
    for char in line:
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            if upper:
                char = char.upper()
            else:
                char = char.lower()
            upper = not upper
        out.append(char)
    print "".join(out)


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        roller_coaster(line.strip())
