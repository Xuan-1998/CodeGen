import sys

n = int(input())
A = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for len_ in range(2, n+1):
    for i in range(n - len_ + 1):
        j = i + len_-1
        if A[j] < A[i]:
            dp[i][j] = dp[i+1][j-1] + 1
        else:
            for k in range(i, j):
                if A[k] > A[i]:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][k-1])
                elif A[k] < A[j]:
                    dp[i][j] = min(dp[i][j], 1 + dp[k+1][j])

print(dp[0][n-1])
