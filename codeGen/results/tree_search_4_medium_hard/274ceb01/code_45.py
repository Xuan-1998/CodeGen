import sys

n = int(input())
marks = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        dp[i][j] = dp[i - 1][min(j, dp[i - 1][i - 1])] + (i - j) * marks[j]

print(min(dp[n]))

