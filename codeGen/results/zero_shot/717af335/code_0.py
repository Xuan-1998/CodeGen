import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

X = 0
Y = A

while True:
    if (X ^ Y) == B:
        print(f"{X} {Y}")
        break
    elif X > B:
        print(-1)
        break
    X += 1
