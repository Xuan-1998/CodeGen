m, N = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i-1][j] + ((j <= a[i-1]) * dp[i-1][j-a[i-1]])) % (10**9 + 7)

print(dp[m][N])
