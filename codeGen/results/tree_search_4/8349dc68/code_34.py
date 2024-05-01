===BEGIN CODE===
def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if j < i:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-k] + max(arr[j-k+1:j]), arr[j])
    
    return dp[n][n]

arr = list(map(int, input().split()))
k = int(input())
print(maxSumAfterPartitioning(arr, k))
===END CODE===
