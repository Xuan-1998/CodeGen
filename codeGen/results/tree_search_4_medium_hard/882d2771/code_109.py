import sys

t, l, r = map(int, input().split())

mod = 10**9 + 7

dp = [[0] * (r+1) for _ in range(t+1)]

for i in range(1, t+1):
    for j in range(1, r+1):
        if i == 1:
            dp[i][j] = min((j-1)*i + 1, (j-1)*(i-1) + 2)
        else:
            dp[i][j] = min(dp[i-1][k] + dp[1][j-k] for k in range(j)) - l*(r-j+1)

print(dp[t][r]%mod)
