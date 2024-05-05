import sys
from collections import defaultdict

n, m, c0, d0 = map(int, input().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
stuffing_info = defaultdict(lambda: [0, 0, 0, 0])

for i in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffing_info[i] = [ai, bi, ci, di]

for i in range(1, n+1):
    for j in range(m+1):
        if i < c0:
            dp[i][j] = 0
        else:
            dp[i][j] = max(dp[i-1][j], d0 + (i-c0)//ci)
            if j > 0:
                ai, bi, ci, di = stuffing_info[j-1]
                dp[i][j] = max(dp[i][j], di + min(i-bi, ci))

print(max(sum(row) for row in dp))
