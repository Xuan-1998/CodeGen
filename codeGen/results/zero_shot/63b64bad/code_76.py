import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for _ in range(n-1):
    x, y = 1, 0
    while x > 0 and x <= n:
        x += a[x]
        y += a[x] - x
        x -= a[x]
    print(y) if x <= 0 or x > n else print(-1)
