import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

for i in range(2, n + 1):
    x, y = 1, 0
    while True:
        a_x = sequence[i - 1]
        x += a_x
        y += a_x
        if x <= 0 or x > n:
            break
        x -= a_x

    print(y)
