import sys

A = int(input())
B = int(input())

min_X = min(A, B)
X = 0
while X <= min_X:
    Y = A - X
    if (X ^ Y) == B:
        print(f"{X} {Y}")
        sys.exit()
    X += 1

print(-1)
