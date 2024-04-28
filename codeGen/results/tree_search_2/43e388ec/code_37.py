import sys

n, m = map(int, input().split())
a = int(input(), 2)
b = int(input(), 2)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(m+1):
        if i < j:
            dp[i][j] = dp[0][0]
        else:
            dp[i][j] = (a >> (i-1)) & 1 ^ ((b >> (j-1)) & 1) + dp[i-1][0]

ans = sum(dp[n][j] for j in range(m+1))
print(ans % (10**9 + 7))
