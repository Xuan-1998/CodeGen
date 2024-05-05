import sys

n, m = map(int, input().split())
a = list(input())
b = list(input())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

lcs_length = dp[n][m]
similarity_score = 4 * lcs_length - (n + m)
print(similarity_score)
