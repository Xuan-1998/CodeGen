def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(n):
        currentMax = arr[i]
        for j in range(1, min(i+1, k)+1):
            currentMax = max(currentMax, arr[i-j+1])
            dp[i+1] = max(dp[i+1], dp[i-j]+currentMax)
    
    return dp[-1]

arr = list(map(int, input().split()))
k = int(input())
print(maxSumAfterPartitioning(arr, k))
