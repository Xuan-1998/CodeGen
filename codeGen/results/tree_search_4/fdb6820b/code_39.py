import sys

m, N = map(int, input().split())
dp = [[0 for _ in range(N+1)] for _ in range(m+1)]
dp[0][0] = 1

for i in range(1, m+1):
    for j in range(N+1):
        dp[i][j] = sum(dp[k][j-1] if k < i else 0 for k in range(i)) + (1 if j == 0 else dp[i-1][j-1])

print((dp[m][N]) % (10**9 + 7))
