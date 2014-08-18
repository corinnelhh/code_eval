# https://www.codeeval.com/open_challenges/126/

# Play with DNA
# Challenge Description:

# The following problem is related to bioinformatics tasks, and in order to
# help in DNA research you will be asked to write an algorithm to find all
# occurrences of the DNA segment in a given DNA string. But it would be too
# easy for you. So please write an algorithm to find all occurrences of
# segment S in DNA string, with maximum allowed mismatches of M. By
# mismatch we understand the minimum of total number of substitutions,
# deletions, insertions necessary to perform on the DNA slice in order to
# completely match the given segment. You need to look at the DNA slices
# with the same length as a given pattern. E.g. the segments 'AGTTATC' ->
# 'AGTATGC' have only 2 mismatches.
# For the DNA string 'CGCCCGAATCCAG' and the segment 'CCC' the first match
# with the maximum allowed mismatch of '1' is 'CGC', the second one is 'GCC',
# the third one is 'CCC' and so on. E.g.

# CCC -> CGC # One mismatch
# CCC -> GCC # One mismatch
# CCC -> CCC # 0 mismatch

# For the given segment 'CCC', the DNA string 'CGCCCGAATCCAG' and the
# maximum allowed mismatch of '1' the list of the matches is
# 'CGC GCC CCC CCG TCC CCA'
# Input sample:

# CCC 1 CGCCCGAATCCAG
# GCGAG 2 CCACGGCCTATGTATTTGCAAGGATCTGGGCCAGCTAAATCAGCACCCCTGGAACGGCAAGGTTCATTTTGTTGCGCGCATAG
# CGGCGCC 1 ACCCCCGCAGCCATATGTCCCCAGCTATTTAATGAGGGCCCCGAACACGGGGAGTCTTACACGATCTGCCCTGGAATCGC

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains a segment of DNA, the maximum allowed
# mismatches M and the DNA string, separated by whitespace. E.g.
# Output sample:

# Print out all the occurrences of a segment S in the DNA string in order
# from the best match,separated by whitespace, taking into account the number
# of allowed mismatches. In case of several segments with the equal matches
# print them in alphabetical order. Print out 'No match' if there is no such
# occurrence. E.g.

# CCC CCA CCG CGC GCC TCC
# GCAAG GCAAG GCCAG GCGCG GCGCA GCTAA
# No match

# Constrains:
# The DNA string length is in range [100, 300]
# The M is in range [0, 40]
# The segment S length is in range [3, 50]


import sys


def get_dna_matches(line):
    segment, m, dna_string = line.split()
    matches = []
    for i in range(len(dna_string) - len(segment)):
        poss_match, mismatches = dna_string[i:i + len(segment)], 0
        for idx, char in enumerate(poss_match):
            if char != segment[idx]:
                mismatches += 1
        if mismatches <= int(m):
            tup = poss_match, mismatches
            matches.append(tup)
    if len(matches):
        matches.sort(key=lambda x: (x[1], x))
        matches = [x[0] for x in matches]
        return " ".join(matches)
    else:
        return "No match"


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            print get_dna_matches(line)


