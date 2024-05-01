def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0, 0] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j]), arr[i-1]
            else:
                dp[i][j] = max(dp[i-1][j-1][0], arr[i-1]), dp[i-1][j-1][0] + arr[i-1]

    return sum(max(row) for row in dp)
