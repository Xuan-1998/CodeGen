import sys

A, B = map(int, input().split())
X = 0
Y = A

while True:
    if B == X ^ Y:
        break
    Y += 1

if Y > A:
    print(-1)
else:
    print(f"{X} {Y}")
