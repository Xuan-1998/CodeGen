import sys

N = int(input())
str1 = input()
str2 = input()

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(i, N + 1):
        for k in range(1, min(i, j) + 1):
            if str1[i - k:i].endswith(str2[j - k:j]):
                dp[i][j] = max(dp[i][j], dp[i - k][j - k] + 1)

print(dp[N][N])
