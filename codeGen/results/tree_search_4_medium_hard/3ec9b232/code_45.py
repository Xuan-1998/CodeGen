import math

n = int(input())
m = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for j in range(1, n+1):
    for i in range(j+1):
        k = min(i+1, m[j])
        dp[i][j] = sum((i-1)!/(k!(i-k-1)!) * (m[j] == m_k ? dp[k][j-1] + dp[i-k-1][j-1] : 0))
            for k in range(k+1)

print(dp[0][n]%10**9+7)
