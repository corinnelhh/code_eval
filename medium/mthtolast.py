import sys


def mth_to_last(line):
    line = line.split()
    num = int(line[-1]) + 1
    if num <= len(line):
        print line[- num]

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_:
        for line in input_.readlines():
            mth_to_last(line)
