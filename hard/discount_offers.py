# https://www.codeeval.com/open_challenges/48/

# Discount Offers
# Challenge Description:

# Our marketing department has just negotiated a deal with several local
# merchants that will allow us to offer exclusive discounts on various
# products to our top customers every day. The catch is that we can only
# offer each product to one customer and we may only offer one product to
# each customer.

# Each day we will get the list of products that are eligible for these
# special discounts. We then have to decide which products to offer to
# which of our customers. Fortunately, our team of highly skilled
# statisticians has developed an amazing mathematical model for
# determining how likely a given customer is to buy an offered product by
# calculating what we call the "suitability score" (SS). The top-secret
# algorithm to calculate the SS between a customer and a product is this:

# 1. If the number of letters in the product's name is even then the SS
# is the number of vowels (a, e, i, o, u, y) in the customer's name
# multiplied by 1.5.
# 2. If the number of letters in the product's name is odd then the SS is
# the number of consonants in the customer's name.
# 3. If the number of letters in the product's name shares any common
# factors (besides 1) with the number of letters in the customer's name
# then the SS is multiplied by 1.5.

# Your task is to implement a program that assigns each customer a product
# to be offered in a way that maximizes the combined total SS across all
# of the chosen offers. Note that there may be a different number of
# products and customers. You may include code from external libraries
# as long as you cite the source.
# Input sample:

# Your program should accept as its only argument a path to a file. Each
# line in this file is one test case. Each test case will be a comma
# delimited set of customer names followed by a semicolon and then a
# comma delimited set of product names. Assume the input file is ASCII
# encoded. For example (NOTE: The example below has 3 test cases):

# Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,
# Nerf Crossbow

# Jeffery Lebowski,Walter Sobchak,Theodore Donald Kerabatsos,Peter Gibbons,
# Michael Bolton,Samir Nagheenanajar;Half & Half,Colt M1911A1,
# 16lb bowling ball,Red Swingline Stapler,Printer paper,
# Vibe Magazine Subscriptions - 40 pack

# Jareau Wade,Rob Eroh,Mahmoud Abdelkader,Wenyi Cai,Justin Van Winkle,
# Gabriel Sinkin,Aaron Adelson;Batman No. 1,Football - Official Size,
# Bass Amplifying Headphones,Elephant food - 1024 lbs,
# Three Wolf One Moon T-shirt,Dom Perignon 2000 Vintage

# Output sample:

# For each line of input, print out the maximum total score to two
# decimal places. For the example input above, the output should look
# like this:

# 21.00
# 83.50
# 71.25

import sys
import itertools as it
from string import letters


def get_score(name, prod):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    prod_lets = [l for l in prod if l in letters]
    name_lets = [l for l in name if l in letters]
    l_p, l_n = len(prod_lets), len(name_lets)
    cons_count = len([1 for let in name_lets if let.lower() not in vowels])
    ss = cons_count if l_p % 2 else (l_n - cons_count) * 1.5
    for i in range(2, min(l_n, l_p) + 1):
        if not l_n % i:
            if not l_p % i:
                return ss * 1.5
    return ss


def get_max_discount(line):
    ll = [el.split(',') for el in line.strip().split(';')]
    max_score = 0
    lim = min(len(ll[0]), len(ll[1]))
    prod_scores = {(n, p): get_score(n, p) for p in ll[1] for n in ll[0]}
    names = [n for n in it.combinations(ll[0], lim)]
    for p_set in it.permutations(ll[1]):
        for name in names:
            z = zip(name, p_set)
            max_score = max(max_score, sum([prod_scores[tup] for tup in z]))
    print "%.2f" % max_score


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            get_max_discount(line)
