code
import sys

n = int(input())
A = input().strip()
m = int(input())
B = input().strip()

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 4
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) - (i+j)
        if i < j:
            dp[i][j] = max(0, dp[i][j])

print(max(0, dp[-1][-1]))
