def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(n - k + 1):
        dp[i + k] = max(dp[i] + arr[i], dp[i])
        
    return dp[-1]

k, n = map(int, input().split())
arr = list(map(int, input().split()))
print(maxSumAfterPartitioning(arr, k))
