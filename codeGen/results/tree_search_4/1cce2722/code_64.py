import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(2, n+1):
    for k in range(1, i+1):
        if a[i] == a[k-1]:
            dp[i][k] = max(dp[k-1][0], dp[i][k-1]) + (i-k+1)
        else:
            dp[i][k] = dp[i-1][k]

memo = [max(dp[i][j] for j in range(n+1)) for i in range(n+1)]

print(max(memo))
