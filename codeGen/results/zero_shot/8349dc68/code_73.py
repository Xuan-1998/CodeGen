def max_sum_after_partitioning(arr, k):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [[0, i] for i in range(n)]
    for j in range(1, n):
        if j - dp[j - 1][1] > k:
            dp[j][0] = max(dp[j-1][0], arr[dp[j-1][1]])
        else:
            dp[j][0] = prefix_sum[j] - prefix_sum[dp[j-1][1]]
    return max([x[0] for x in dp])
