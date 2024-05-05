import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

X = 0
while X <= max(A, B):
    Y = A - X
    if (X ^ Y) == B:
        print(f"{X} {Y}")
        sys.exit(0)
    X += 1

print(-1)
