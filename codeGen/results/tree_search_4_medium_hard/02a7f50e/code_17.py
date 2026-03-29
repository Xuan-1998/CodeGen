n = int(input())
dp = [[float('inf')] * (1000010) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(1, 1000001):
        dp[i][j] = float('inf')
        for k in range(i):
            if j <= dp[k][min(j, 1000000)]:
                dp[i][j] = min(dp[i][j], (i-k-1) + dp[k][min(j, 1000000)])

print(min(dp[n]))
