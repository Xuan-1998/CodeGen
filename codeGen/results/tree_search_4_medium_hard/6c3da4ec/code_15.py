import sys

n = int(input())
s = input()

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    dp[i][i] = s[i]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length
        max_or = 0
        for k in range(i + 1, j):
            or_val = int(s[i:k], 2) | int(s[k:j], 2)
            max_or = max(max_or, or_val)
        dp[i][j - 1] = max_or

print(bin(dp[0][n - 1])[2:].zfill(n))
