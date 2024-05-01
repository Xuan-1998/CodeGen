import sys
input = lambda: [int(x) for x in input().split()]
m, N = input()
dp = [[0]*(N+1) for _ in range(m+1)]

for i in range(m+1):
    dp[i][0] = 1

for i in range(1, m+1):
    for j in range(N+1):
        if j >= i:
            dp[i][j] = (dp[i-1][j-i] + dp[i-1][j]) % (10**9 + 7)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[m][N])
