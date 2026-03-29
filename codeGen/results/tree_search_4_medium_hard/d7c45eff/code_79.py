import sys

n, k = map(int, input().split())
s = input()

dp = [["" for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    if i == 0:
        dp[i][k] = ""
    elif k-i >= 0 and s[i-1] <= s[k-1]:
        dp[i][k] = min(s[:i], s[k-i:]) if i > 0 else s[:min(i, k)]
    else:
        dp[i][k] = min(s[:i], s)

print(dp[n][k])
