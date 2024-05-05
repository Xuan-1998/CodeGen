import sys
from collections import defaultdict

n, q, c = map(int, input().split())
stars = defaultdict(lambda: [0] * (c + 1))

for _ in range(n):
    x, y, s = map(int, input().split())
    for i in range(s, min(c, s + 9) + 1):
        stars[(x, y)][i] += 1

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    views.append((t, (x1, y1), (x2, y2)))

dp = [[[0] * (c + 1) for _ in range(101)] for _ in range(101)]

for star in stars:
    x, y = star
    for i in range(min(c, s + 9) + 1):
        dp[100][y][i] += stars[star][i]

for t in range(q - 1):
    for x in range(1, 101):
        for y in range(1, 101):
            if dp[t][y][c]:
                dp[t + 1][x][c] = dp[t][y][c]
            else:
                dp[t + 1][x][c] = 0
            for i in range(c - 9, -1, -1):
                if dp[t][y][i]:
                    dp[t + 1][x][c] += dp[t][y][i]
                else:
                    break

for view in views:
    t, (x1, y1), (x2, y2) = view
    print(sum(dp[t][y][c] for y in range(min(y2, y1 - 9) + 1)))
