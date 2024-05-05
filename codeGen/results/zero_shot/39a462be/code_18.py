import sys
n = int(input())
m = int(input())
A = input().strip()
B = input().strip()

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

max_score = 0
for i in range(n + 1):
    for j in range(m + 1):
        lcs_length = dp[i][j]
        score = 4 * lcs_length - (i + j)
        max_score = max(max_score, score)

print(max_score)
