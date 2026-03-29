import sys

n, q, c = map(int, sys.stdin.readline().split())
stars = []
for _ in range(n):
    x, y, s = map(int, sys.stdin.readline().split())
    stars.append((x, y, s))

views = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    views.append(((t, (x1, y1), (x2, y2)), 0))  # Initialize the view's brightness to 0

dp = [[0] * (q + 1) for _ in range(q + 1)]

for i in range(n):
    x, y, s = stars[i]
    for j in range(q):
        t, ((x1, y1), (x2, y2)) = views[j]
        if x1 <= x <= x2 and y1 <= y <= y2:  # Star is visible
            dp[views[j][0][0]][j] += s
        else:
            dp[views[j][0][0]][j] -= s

ans = 0
for i in range(q):
    ans += dp[i][i]
print(ans)
