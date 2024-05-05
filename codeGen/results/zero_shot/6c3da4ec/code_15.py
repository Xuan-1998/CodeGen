import sys

n = int(input())
s = input()

dp = [[0] * (1 << n) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(2**i - 1, 2**(i-1)):
        if s[j] == '1':
            dp[i][j] = max(dp[i][j], dp[i-1][j//2] | (1 << (i-1)))
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j//2])

max_or = 0
for j in range(2**n - 1, 2**(n-1)):
    max_or = max(max_or, dp[n][j])

print(bin(max_or)[2:])
