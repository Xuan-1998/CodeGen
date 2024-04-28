import sys

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[-float('inf')] * (k + 1) for _ in range(n)]

    for i in range(k - 1, n):
        for j in range(1, min(i - k + 2, k) + 1):
            for last_idx in range(j - 1, i + 1):
                dp[i][j] = max(dp[i][j], dp[last_idx][j - 1] + arr[last_idx:j].max())

    return max(dp[-1])

# Read input from stdin
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(maxSumAfterPartitioning(arr, k))
