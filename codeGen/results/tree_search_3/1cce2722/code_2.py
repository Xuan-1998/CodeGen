from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (106) for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(1, 106):
        if a[i-1] == k:
            dp[i][k] = max(dp[i-1][k-1], dp[i-1][k+1]) + 1
        elif a[i-1] - 1 == k or a[i-1] + 1 == k:
            dp[i][k] = max(dp[i-1][k-1], dp[i-1][k+1]) + 1
        else:
            dp[i][k] = dp[i-1][k]

print(max(dp[n]))
