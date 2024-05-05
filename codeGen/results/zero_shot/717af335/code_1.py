import math

A = int(input())
B = int(input())

X = A // 2
Y = A - X

A_XOR_B = A ^ B

while True:
    if X ^ Y == A_XOR_B:
        break
    else:
        X ^= (A - X) // 2

print(X, Y)
