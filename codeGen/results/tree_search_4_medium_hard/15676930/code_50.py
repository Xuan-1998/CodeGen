import sys

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][1] = c[0]
    for j in range(2, min(i+1, n)+1):
        max_joy = 0
        for k in range(max(0, i-j), i):
            max_joy = max(max_joy, dp[k][j-1] + (a[i-k] if j == 2 else b[i-k]))
        dp[i][j] = max(dp[i-1][j-1] + c[0], max_joy)

print(max(0, *dp[n]))
