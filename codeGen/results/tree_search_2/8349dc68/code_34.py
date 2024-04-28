def max_sum_subarray(arr, k):
    n = len(arr)
    dp = {0: 0}
    res = 0

    for i in range(n):
        if i >= k:
            dp[i-k+1] = max(dp[i-k+1], dp[i-k]+arr[i])
        else:
            dp[i+1] = arr[i]

        res = max(res, dp[i+1])

    return res
