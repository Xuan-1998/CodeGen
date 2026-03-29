import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

x = 0
y = A

while True:
    if x ^ y == B:
        print(f"{x} {y}")
        break
    elif x < (2 ** 63 - 1):
        y += 1
    else:
        print(-1)
        break
