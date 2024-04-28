import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (max(a) + 1) for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(min(a), max(a)+1):
        if a[i-1] == k:
            dp[i][k] = dp[i-1][k-1] + 3 if k > 1 else dp[i-1][k]

print(max(dp[-1]))
