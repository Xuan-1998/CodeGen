import sys

n, m = map(int, input().split())
dp = [[0]*m for _ in range(n+1)]
sectioning_points = [0]*m
last_s = 1

for i in range(1, n+1):
    s, x = map(int, input().split())
    if s != last_s:
        for j in range(m-1, sectioning_points[last_s-1], -1):
            dp[i][s] = min(dp[i][s], dp[j][last_s-1] + 1)
            sectioning_points[s] = max(sectioning_points[s], i)
    else:
        dp[i][s] = dp[i-1][s]
    last_s = s

print(min([dp[i][s] for i in range(n) for s in range(1, m+1)]))
