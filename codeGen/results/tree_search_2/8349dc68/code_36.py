def maxSumAfterPartition(arr, k):
    n = len(arr)
    dp = {0: 0}
    
    for i in range(1, n+1):
        if i <= k:
            dp[i] = max(dp.get(i-1, 0), arr[i-1])
        else:
            dp[i] = max(dp.get(i-k, 0), arr[i-1])
            
    return sum(dp.values())

# Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(maxSumAfterPartition(arr, k))
