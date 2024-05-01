import sys

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], arr[i - 1])
            else:
                dp[i][j] = max(dp[i - 1][j - 1], arr[i - 1]) + dp[i - 1][0]

    return max(dp[-1])

# read inputs
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(maxSumAfterPartitioning(arr, k))
