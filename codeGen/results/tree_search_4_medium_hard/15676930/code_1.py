import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = max(dp[i-1][0], b[i-1])
    if i == 1:
        dp[i][1] = a[0]
    else:
        dp[i][1] = max(dp[i-1][1], c[i-2] + a[i-1])

for i in range(1, n + 1):
    for j in range(1, min(i + 1, n) + 1):
        if i == 1:
            dp[i][j] = max(dp[i][0], dp[0][j])
        else:
            dp[i][j] = max(dp[i-1][0], dp[i-2][1] + a[i-1])

print(max(dp[n]))
