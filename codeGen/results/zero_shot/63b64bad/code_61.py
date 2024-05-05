import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

max_y = -1
for a in sequence:
    x, y = 1, 0
    while True:
        if x <= 0 or x > n:
            break
        x += a
        y += a
        x -= a
    max_y = max(max_y, y)

print(max_y)
