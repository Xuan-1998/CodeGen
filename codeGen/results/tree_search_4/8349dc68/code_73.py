def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_val = 0
        for j in range(min(i, k), 0, -1):
            max_val = max(max_val, arr[i - j])
            dp[i][j] = max(dp[i][j], dp[i - j][j - 1] + max_val * j)
    return dp[-1][-1]

# Read input from stdin
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(maxSumAfterPartitioning(arr, k))
