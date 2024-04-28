import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0, 0]] * (n + 1)
dp[1][0] = a[0]
for i in range(2, n + 1):
    dp[i][0] = max(dp[i-1][0], dp[i-2][1])
    if a[i] == a[i-1] + 1 or a[i] == a[i-1] - 1:
        dp[i][1] = dp[i-1][0]
    else:
        dp[i][1] = max(dp[i-1][0], dp[i-2][1])

print(max(dp[n]))
