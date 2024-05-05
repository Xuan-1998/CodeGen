from collections import defaultdict

n, m, c0, d0 = map(int, input().split())
dp = defaultdict(lambda: defaultdict(int))

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    dp[0][0] = max(dp[0][0], 0) + d0
    for i in range(n+1):
        for j in range(1, m+1):
            if j > 0:
                dp[i][j] = max(dp[max(i-ci[j], 0)][j-1], dp[i-c0][0]) + di
            else:
                dp[i][0] = max(dp[max(i-c0, 0)][0], 0) + d0

print(max(0 for i in range(n+1) for j in range(m+1) if dp[i][j]))
