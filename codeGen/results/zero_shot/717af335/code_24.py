import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

for X in range(A + 1):
    Y = A - X
    if ((X ^ Y) == B):
        print(f"{X} {Y}")
        break
else:
    print(-1)
