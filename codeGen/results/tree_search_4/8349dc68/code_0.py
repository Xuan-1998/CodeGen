from collections import defaultdict

def maxSumAfterPartition(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    # Initialize the base case
    dp[0] = 0
    
    for i in range(1, n + 1):
        max_sum = float('-inf')
        for j in range(i):
            if j + k <= i:
                max_sum = max(max_sum, dp[j] + max(arr[j:j+k]))
        dp[i] = max_sum
    return dp[n]

arr = list(map(int, input().split()))
k = int(input())
print(maxSumAfterPartition(arr, k))
