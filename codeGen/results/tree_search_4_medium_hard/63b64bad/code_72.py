from collections import defaultdict

n = int(input())
dp = {(1, 0): 0}
x, y = 1, 0
for _ in range(2, n+1):
    x -= a[_]
    y += a[_]
    dp[(x, y)] = y
    if x <= 0 or x > n:
        print(y)
        break
else:
    print(-1)
