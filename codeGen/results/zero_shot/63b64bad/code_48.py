import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

y_max = -1

for i in range(2, n+1):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > i:
            break
        x += sequence[x]
        y += sequence[x]
        y -= sequence[x]

    y_max = max(y_max, y)

print(y_max)
