import sys

def min_operations(A):
    n = len(A)
    dp = [[0] * (max(A) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max(A) + 1):
            if A[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][k - 1] + 1 for k in range(1, j + 1) if A[k - 1] < A[k])

    return dp[n][max(A)]

# Read input from stdin
n = int(input())
A = list(map(int, input().split()))

print(min_operations(A))
