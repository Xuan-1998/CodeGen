n, m = map(int, input().split())
dp = [[0] * (m+1) for _ in range(n+1)]

for i from 1 to n:
    for j from 1 to m:
        dp[i][j] = min(dp[max(0, i-1)][j] + dp[i][max(0, j-1)]) + 1

print(dp[n][m])
