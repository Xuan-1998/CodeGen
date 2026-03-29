import sys

A, B = map(int, sys.stdin.readline().split())
X = (B << 1) + A
Y = X ^ B

print(f"{X} {Y}")
