# https://www.codeeval.com/open_challenges/110/

# Text to Number
# Challenge Description:

# You have a string which contains a number represented as English text.
# Your task is to translate these numbers into their integer representation.
# The numbers can range from negative 999,999,999 to positive 999,999,999.
# The following is an exhaustive list of English words that your program
# must account for:

# negative,
# zero, one, two, three, four, five, six, seven, eight, nine,
# ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,
# eighteen, nineteen,
# twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety,
# hundred,
# thousand,
# million

# Input sample:

# Your program should accept as its first argument a path to a filename.
# Input example is the following

# fifteen
# negative six hundred thirty eight
# zero
# two million one hundred seven

# - Negative numbers will be preceded by the word negative.
# - The word "hundred" is not used when "thousand" could be. E.g. 1500 is
# written "one thousand five hundred", not "fifteen hundred".
# Output sample:

# Print results in the following way.

# 15
# -638
# 0
# 2000107


import sys

nums = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 16, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90
}

places = {"hundred": 100, "thousand": 1000, "million": 1000000}


def get_num(phrase):
    total, int_sum = 0, 0
    negative = False
    for word in phrase.split():
        if word == 'negative':
            negative = True
        elif word in nums:
            int_sum += nums[word]
        elif word in places:
            int_sum *= places[word]
        if word == "thousand" or word == "million":
            total += int_sum
            int_sum = 0
    total += int_sum
    if negative:
        return total * -1
    else:
        return total

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for line in lines:
        print get_num(line)
