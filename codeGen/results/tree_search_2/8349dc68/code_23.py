import sys

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = {0: arr[0]}
    
    for i in range(1, n):
        dp[i] = max(dp.get(i-1, 0), arr[i])
        for j in range(min(i+1, k), 0, -1):
            if j <= i:
                dp[i] = max(dp[i], dp.get(i-j, 0) + min(arr[i-j+1:i+1]))
    
    return sum(dp.values())

k = int(input())
n = int(input())
arr = list(map(int, input().split()))

print(maxSumAfterPartitioning(arr, k))
