import sys

A, B = map(int, sys.stdin.readline().split())
X = ((B << 1) + A) >> 2
Y = A - X

if X >= 0 and Y >= 0:
    print(X, Y)
else:
    print(-1)
