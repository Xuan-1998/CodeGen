import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

for i in range(n - 1):
    x = y = 0
    while True:
        if x <= 0 or x > n:
            break
        x += a[x]
        y += a[x]
        x -= a[x]
    print(y)
