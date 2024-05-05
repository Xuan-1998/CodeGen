import sys

def min_operations():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(i, N+1):
            if A[j-1] > A[j]:
                dp[i][j] = 1 + dp[i][j-1]
            else:
                min_ops = float('inf')
                for k in range(j):
                    if A[k] > A[k+1]:
                        min_ops = min(min_ops, dp[k][j-1] + (A[j-1] - A[j]))
                dp[i][j] = min(dp[i-1][j], min_ops)

    return dp[N][N]

print(min_operations())
