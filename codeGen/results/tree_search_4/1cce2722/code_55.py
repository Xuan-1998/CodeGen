import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (n - 1) for _ in range(n)]

for i in range(1, n - 1):
    for j in range(2, n - 2):
        if a[i] == a[j-1] or a[i] == a[j+1]:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j+1]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j+1])

print(max(dp[-1]))
