def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = {0: 0}
    for i in range(1, n+1):
        dp[i] = max(dp.get(i-1, 0), arr[i-1])
        if i >= k:
            dp[i] += sum(arr[max(0, i-k):i])
    return max(dp.values())
