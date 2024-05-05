import sys

# Read input
n, q, c = map(int, input().split())
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

dp = [[0] * (c+1) for _ in range(101*101)]

# Calculate initial brightness for each star
for x, y, s in stars:
    dp[y][s] += 1

# Iterate over all views and calculate total brightness
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1-1, y2+1):
        for j in range(min(x1-1, 100), max(x2, 100)+1):
            if dp[i][j]:
                dp[y2][min(c, sum(dp[i][k] for k in range(j, min(x2, 100)+1)))]

# Print total brightness for each view
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    print(sum(dp[y][t] for y in range(y1-1, y2+1)))
