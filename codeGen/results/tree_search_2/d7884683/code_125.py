def max_partitions(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        
        if left_sum % 2 == 0 and right_sum % 2 == 0:
            dp[i] = max(dp[i-1], 1 + min([dp[j] for j in range(i)]))
        else:
            dp[i] = dp[i-1]

    return dp[-1]
