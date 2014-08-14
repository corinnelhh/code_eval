import sys


def print_lines(lines):
    n = int(lines[0])
    lines = lines[1:]
    lines.sort(key=len)
    count = 0
    for line in lines[::-1]:
        count += 1
        print line
        if count >= n:
            break


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

        print_lines(lines)
