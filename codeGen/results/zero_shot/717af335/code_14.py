import sys

A = int(input())
B = int(input())

if A % 2 == 0:
    X = 0
    Y = A
else:
    X = A // 2 + (1 if B < A else 0)
    Y = A - X

print(X, Y)
