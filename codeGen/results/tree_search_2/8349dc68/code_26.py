def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            max_val = float('-inf')
            for window_start in range(max(0, i - k), i):
                max_val = max(max_val, dp[window_start][j - 1] + max(arr[window_start:i]))
            dp[i][j] = max_val
    
    return max(dp[-1])

arr = list(map(int, input().split()))
k = int(input())
print(maxSumAfterPartitioning(arr, k))
