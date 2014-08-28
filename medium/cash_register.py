# https://www.codeeval.com/open_challenges/54/

# Cash Register
# Challenge Description:

# The goal of this challenge is to design a cash register program. You
# will be given two float numbers. The first is the purchase price (PP)
# of the item. The second is the cash (CH) given by the customer. Your
# register currently has the following bills/coins within it:

# 'PENNY': .01,
# 'NICKEL': .05,
# 'DIME': .10,
# 'QUARTER': .25,
# 'HALF DOLLAR': .50,
# 'ONE': 1.00,
# 'TWO': 2.00,
# 'FIVE': 5.00,
# 'TEN': 10.00,
# 'TWENTY': 20.00,
# 'FIFTY': 50.00,
# 'ONE HUNDRED': 100.00

# The aim of the program is to calculate the change that has to be
# returned to the customer.

# Input sample:

# 15.94;16.00
# 17;16
# 35;35
# 45;50

# Your program should accept as its first argument a path to a filename.
# The input file contains several lines. Each line is one test case. Each
# line contains two numbers which are separated by a semicolon. The first
# is the Purchase price (PP) and the second is the cash(CH) given by the
# customer. eg.
# Output sample:

# NICKEL,PENNY
# ERROR
# ZERO
# FIVE

# For each set of input produce a single line of output which is the
# change to be returned to the customer. In case the CH < PP, print out
# ERROR. If CH == PP, print out ZERO. For all other cases print the amount
# that needs to be returned, in terms of the currency values provided. The
# output should be sorted in highest-to-lowest order (DIME,NICKEL,PENNY).
# eg.

import sys


def get_change(line):
    register = {
        'PENNY': .01,
        'NICKEL': .05,
        'DIME': .10,
        'QUARTER': .25,
        'HALF DOLLAR': .50,
        'ONE': 1.00,
        'TWO': 2.00,
        'FIVE': 5.00,
        'TEN': 10.00,
        'TWENTY': 20.00,
        'FIFTY': 50.00,
        'ONE HUNDRED': 100.00
    }

    price, cash = line.split(";")
    price, cash = float(price), float(cash)
    change = cash - price
    if change < 0:
        return 'ERROR'
    elif change == 0:
        return 'ZERO'
    coins = []
    for denom, value in sorted(
            register.items(), key=lambda x: x[1], reverse=True):
    ##The string-float-int coercions are a hack to get around floating
    ##point division errors
        units = int(float(str(change)) / float(str(value)))
        for i in range(units):
            coins.append(denom)
        change -= round(units * value, 2)
    return ",".join(coins)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            print get_change(line.strip())

