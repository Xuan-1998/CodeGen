import sys

def max_sum_of_subarrays(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i <= k:
            dp[i] = max(dp[i - 1], sum(arr[:i]))
        else:
            dp[i] = max(dp[i - 1], dp[i - k] + arr[i - 1])
            
    return dp[n]

k = int(input())
arr = list(map(int, input().split()))
print(max_sum_of_subarrays(arr, k))
