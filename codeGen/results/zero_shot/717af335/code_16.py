import sys

A = int(input())
B = int(input())

X = 0
while True:
    Y = A - X
    if B == X ^ Y:
        print(f"{X} {Y}")
        break
    elif X > B:
        print(-1)
        break
    X += 1
