import sys

N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 10000001 for _ in range(N)]

for i in range(1, N):
    min_ops = float('inf')
    for j in range(A[i-1]+1, A[i]+1):
        for k in range(A[i-1]+1, j+1):
            dp[i][j] = min(dp[i][j], dp[i-1][k] + (A[i]-j))
        if dp[i][j] < min_ops:
            min_ops = dp[i][j]
    dp[i][A[i]] = min_ops + 1

print(dp[N-1][A[N-1]])
