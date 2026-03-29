import sys
from collections import defaultdict

# Read input
n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    x1, y1, x2, y2, t = map(int, sys.stdin.readline().split())

# Initialize 3D array for dynamic programming
dp = [[[0] * (c + 1) for _ in range(101)] for _ in range(101)]

for x1, y1, s in stars:
    for t in range(s, c + 1):
        dp[y1][x1][t] += s

for x1, y1, x2, y2, t in views:
    total_brightness = sum(sum(dp[y][i][t] - dp[y][min(i-1, 100)][t] for i in range(x1, x2+1)) for y in range(y1, y2+1))
    print(total_brightness)
