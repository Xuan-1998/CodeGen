def min_operations(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = min(dp[i], dp[j-1] + 1) if j > 0 else 1
    return dp[-1]
