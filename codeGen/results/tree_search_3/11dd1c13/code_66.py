import sys

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][0] = A[i][0]
for j in range(1, n):
    for k in range(j):
        if A[i-1][k] != A[i-1][j]:
            dp[i][j] = min(dp[i][j], dp[i-1][k] + A[i][j])
print(min([x[-1] for x in dp]))
