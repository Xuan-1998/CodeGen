def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i - j <= k:
                dp[i][j] = max(dp[i-1][k-1] + arr[i-j:i+1])
            else:
                dp[i][j] = dp[i-1][j-1] + arr[i-j:i]
    
    return dp[n-1][k-1]

# Read input from standard input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(maxSumAfterPartitioning(arr, k))
