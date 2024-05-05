import sys
input = lambda: [int(x) for x in input().split()]
n = input()[0]
m = list(input())

dp = [[0] * (n+1) for _ in range(n+1)]
dp[1][1] = 1

for i in range(2, n+1):
    for j in range(i+1):
        if m[i-1] == i:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] += dp[i-1][j]
dp[n][0] %= (10**9 + 7)
print(dp[n][0])
