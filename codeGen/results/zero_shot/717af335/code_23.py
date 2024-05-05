import sys

def find_X(A, B):
    # The idea is to use bitwise operation
    X = A - ((A ^ B) & ((A - 1) ^ (B - 1)))
    Y = A ^ B
    return X, Y

A = int(input())
B = int(input())

X, Y = find_X(A, B)

if X >= 0 and Y >= 0:
    print(X, Y)
else:
    print(-1)
