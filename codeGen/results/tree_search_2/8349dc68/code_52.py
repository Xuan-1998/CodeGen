def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_sum = arr[i - 1]
        for j in range(min(i, k), 0, -1):
            max_sum = max(max_sum, dp[i - j][j - 1] + arr[i - 1])
            dp[i][j] = max_sum

    return dp[n][k]

# test case
arr = list(map(int, input().split()))
k = int(input())
print(maxSumAfterPartitioning(arr, k))
