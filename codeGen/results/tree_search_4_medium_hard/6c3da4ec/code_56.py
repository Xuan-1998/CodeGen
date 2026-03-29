import sys

n = int(input())
s = input()

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(i, n), -1, -1):
        if s[j] == '1':
            dp[i][j] = max(dp[i-1][j], int(s[j]) | dp[i-1][j-1])
        else:
            dp[i][j] = dp[i-1][j]

max_or = 0
for i in range(1, n + 1):
    if s[i-1] == '1':
        max_or = max(max_or, int(s[i-1]) | dp[i-1][i-1])

print(bin(max_or)[2:].zfill(n).lstrip('0') or '0')
