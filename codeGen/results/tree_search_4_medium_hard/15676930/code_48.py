import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = c[i-1]
    for j in range(1, min(i+1, n)+1):
        dp[i][j] = max(dp[k][j-1] + b[i-k] if k < i else c[i-1], 0 <= k < i and dp[k][j-1] + a[i-k] or 0 for k in range(j))

print(max(dp[i][n] for i in range(n+1)))
