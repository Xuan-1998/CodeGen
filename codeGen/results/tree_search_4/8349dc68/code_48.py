def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[-float('inf')] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        if i == 0:
            dp[i][0] = arr[0]
        else:
            dp[i][0] = dp[i - 1][0] + arr[i]

        for j in range(1, min(i + 1, k) + 1):
            if arr[i] <= k:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i])
            else:
                dp[i][j] = dp[i - 1][j]

    return max(dp[-1])

