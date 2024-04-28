k, n = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, k+1):
    if i % k == 0:
        dp[i][i] = (n // i) + 1
        for j in range(i+1, k+1):
            dp[j][j] += dp[i][i]
    else:
        dp[i][i] = 0

for i in range(1, n+1):
    for j in range(2, min(i+1, k)+1):
        if i % j == 0:
            dp[i][j] = (dp[i//j][j-1] + (n // i)) % 1000000007
        else:
            dp[i][j] = 0

print((dp[n][k]) % 1000000007)
