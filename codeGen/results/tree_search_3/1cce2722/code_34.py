import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 106 for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(max(a[:i]) + 1):
        if a[i - 1] == k:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - 1] + dp[i - 2][k + 1] if i > 1 and k > 0 else 0)
        else:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - 1] + (a[i - 1] == k - 1) * (dp[i - 2][k + 1] if i > 1 and k > 0 else 0))

print(max(dp[n]))
