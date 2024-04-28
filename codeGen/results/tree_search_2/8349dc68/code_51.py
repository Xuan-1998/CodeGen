def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_val = arr[i - 1]
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = max_val
            else:
                dp[i][j] = max(dp[i - 1][j], max_val)
                for last_idx in range(max(0, i - k), i):
                    dp[i][j] = max(dp[i][j], dp[last_idx][k - 1] + arr[i - 1])
    return dp[-1][-1]

arr = [int(x) for x in input().split()]
k = int(input())
print(maxSumAfterPartitioning(arr, k))
