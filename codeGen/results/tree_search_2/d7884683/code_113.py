def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if prefix_sum[i] - prefix_sum[j] == prefix_sum[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
