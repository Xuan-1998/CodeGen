def min_operations(arr):
    n = len(arr)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]
