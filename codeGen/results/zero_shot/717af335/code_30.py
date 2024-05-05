import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

X = A - (1 << ((~B & 1) + 1))
Y = X ^ B

print(f"{X} {Y}")
