import sys

N = int(input())
str1 = input().strip()
str2 = input().strip()

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = dp[i-1][0]
    dp[0][i] = dp[0][i-1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][N])
