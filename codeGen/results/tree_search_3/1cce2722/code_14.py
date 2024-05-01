import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 107 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1
    for k in range(1, i):
        if a[i - 1] == k:
            dp[i][k] = max(dp[i][k], dp[i - 1][k])
        elif abs(a[i - 1] - k) == 1:
            dp[i][k] = max(dp[i][k], dp[i - 1][k] + 1)
        else:
            dp[i][k] = dp[i - 1][k]

print(max(dp[-1]))
