def max_path_sum(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = arr[i]

    for i in range(1, n):
        for j in range(i):
            if arr[j] > 0:
                max_sum = arr[j]
                for k in range(j+1, i+1):
                    max_sum = max(max_sum, dp[j][k-1] + arr[k])
                dp[i][j] = max_sum
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]
