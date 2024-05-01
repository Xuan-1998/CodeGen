import sys

N = int(input())

str1 = input()
str2 = input()

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif str1[:i] == str2[:j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][N])
