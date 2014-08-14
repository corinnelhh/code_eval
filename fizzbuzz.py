import sys


def fizzbuzz(a, b, n):
    out = []
    for i in xrange(1, n + 1):
        if not i % a and not i % b:
            out.append("FB")
        elif not i % a:
            out.append("F")
        elif not i % b:
            out.append("B")
        else:
            out.append(str(i))
    return " ".join(out)


if __name__ == "__main__":

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        for line in lines:
            a, b, n = line.split()
            print fizzbuzz(int(a), int(b), int(n))
