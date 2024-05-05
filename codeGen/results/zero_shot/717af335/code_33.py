import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

X = min(A // 2, B)
Y = A - X

if (X ^ Y) != B:
    print(-1)
else:
    print(f"{X} {Y}")
