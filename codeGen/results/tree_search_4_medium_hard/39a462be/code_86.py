import sys

A = input().strip()
B = input().strip()

dp = [[[0, []] for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(len(A)+1):
    for j in range(len(B)+1):
        if i == 0 or j == 0:
            dp[i][j] = [0, []]
        elif A[i-1] != B[j-1]:
            dp[i][j] = [max(dp[i-1][j][0], dp[i][j-1][0]), dp[i-1][j-1][1]]
        else:
            if len(dp[i-1][j-1][1]) < 4 + min(i, j):
                dp[i][j] = [dp[i-1][j-1][0], dp[i-1][j-1][1] + [(A[i-2], B[j-2])] ]
            else:
                dp[i][j] = [max(dp[i-1][j-1][0], dp[i-1][j-1][0]), dp[i-1][j-1][1]]

max_score = 0
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if len(dp[i][j][1]) > 0:
            score = 4 * len(dp[i][j][1]) - (i + j)
            max_score = max(max_score, score)

print(max_score)
