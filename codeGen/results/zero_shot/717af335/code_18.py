import sys

def solve():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())

    for x in range(A + 1):
        y = A - x
        if (x ^ y) == B:
            return str(x) + ' ' + str(y)

    return '-1'

print(solve())
