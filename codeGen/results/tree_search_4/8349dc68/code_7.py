import sys

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = max(dp[i-1], dp[max(i-k, 0)] + max(arr[i-k:i]))
    
    return dp[n]

# Read inputs from stdin
k = int(input())
arr = list(map(int, input().split()))

print(maxSumAfterPartitioning(arr, k))
