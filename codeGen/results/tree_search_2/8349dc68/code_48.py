def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i < k:
            dp[i] = sum(arr[:i])
        else:
            dp[i] = max(dp[i - k], sum(arr[i - k:i]))
            for j in range(i - k + 1):
                dp[i] = max(dp[i], sum(arr[j:j+k]) + dp[j-1])

    return dp[n]
