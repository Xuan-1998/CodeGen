import sys
input = lambda: [int(i) for i in input().split()]
n, s = input()
a = input()

dp = [[0] * (s + 1) for _ in range(n)]
for i in range(n):
    for j in range(s + 1):
        if a[i] <= j:
            dp[i][j] = min(dp[(i-1)][j-a[i]] - j + a[i], dp[i-1][j])
        else:
            dp[i][j] = min(dp[i-1][j-s] + s, dp[i-1][j])
print(min(dp[-1]))
