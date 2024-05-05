import sys

def solve():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())

    X = 0
    while X <= A:
        Y = A - X
        if (X ^ Y) == B:
            return f"{X} {Y}"
        X += 1

    return "-1"

print(solve())
