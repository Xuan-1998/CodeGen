def count_subarrays(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if max(arr[:i+1]) > k:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    return dp[-1]
