import sys
from collections import defaultdict

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: subarrays of length j starting from the beginning
    for i in range(1, k + 1):
        dp[0][i] = arr[i - 1]

    for i in range(k, n + 1):
        for j in range(min(i, k), -1, -1):
            dp[i][j] = max(dp[i-1][j-1] + arr[i+j-1], dp[i-1][k-j-1])
    
    return max(sum(arr[i:i+k]) for i in range(n-k+1))

arr = [int(x) for x in input().split()]
k = int(input())

print(maxSumAfterPartitioning(arr, k))
