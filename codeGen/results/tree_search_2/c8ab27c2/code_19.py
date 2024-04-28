code
import sys

S = input().strip()
T = input().strip()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1

print(min(max(dp[i][len(T)] for i in range(len(S) + 1)), default=-1))
