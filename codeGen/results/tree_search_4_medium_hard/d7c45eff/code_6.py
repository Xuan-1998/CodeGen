import sys

n, k = map(int, input().split())
s = input()

dp = [[s[:i]] for i in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = s[:i]
for j in range(1, min(k, n)+1):
        if j < len(s[:n]):
            dp[0][j] = s[:n]
        for i in range(j-1, -1, -1):
            dp[i][j] = min(dp[i][j-1], dp[max(0, j-len(s[:i]))][max(0, j-len(s[:i]))])

print(min(dp[n-1][k-1], s))
