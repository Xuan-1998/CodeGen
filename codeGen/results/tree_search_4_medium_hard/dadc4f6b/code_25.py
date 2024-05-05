import sys

n, q, c = map(int, input().split())
dp = [[[0] * (c + 1) for _ in range(101)] for _ in range(101)]

# Preprocess initial brightness of stars
for _ in range(n):
    x, y, s = map(int, input().split())
    dp[y][x][s] += s

# Process queries
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    total_brightness = 0
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if dp[i][j][t] > 0:
                total_brightness += dp[i][j][t]
    print(total_brightness)
