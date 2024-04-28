def count_subarrays(Arr, K):
    n = len(Arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        max_val = max(Arr[i:])
        for j in range(i, n):
            if Arr[j] > K and max_val > K:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1]
    
    return sum(dp[0])
