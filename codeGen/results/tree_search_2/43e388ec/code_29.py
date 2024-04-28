dp = [[0]*(31) for _ in range(21)]
for i in range(1, 20+1):
    for j in range(min(i, 30)+1):
        if j == 0:
            dp[i][j] = (dp[i-1][0] if i > 1 else 0)
        else:
            dp[i][j] = (dp[i-1][0] if i > 1 else 0) + ((a >> (i-1)) & 1) * ((b >> (i-1)) % (10**9+7))
print(sum((dp[i][j] for i in range(20, -1, -1) for j in range(min(i,30),-1,-1)), default=0, total=(10**9+7)))
