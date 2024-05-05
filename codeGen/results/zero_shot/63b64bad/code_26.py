code
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

x, y = 1, 0

while True:
    if x <= 0 or x > n:
        break
    x += sequence[x-1]
    y += sequence[x-1]
    x -= sequence[x-1]
    y += sequence[x-1]

if x > n:
    print(-1)
else:
    print(y)
