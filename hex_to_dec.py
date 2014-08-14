#https://www.codeeval.com/open_challenges/67/
import sys


def hex_to_dec(hex_num):
    conv = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15
    }
    dec_num = 0
    count = 1
    for dig in hex_num[::-1]:
        dec_num += conv[dig] * count
        count *= 16
    return dec_num

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    for line in f.read().strip().split("\n"):
        print hex_to_dec(line)
    f.close()
