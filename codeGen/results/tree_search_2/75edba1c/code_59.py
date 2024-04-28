import sys

def count_subarrays(arr, K):
    n = len(arr)
    dp = [0] * (n + 1)
    
    max_val = -float('inf')
    for i in range(n):
        if arr[i] > K and arr[i] > max_val:
            max_val = arr[i]
            dp[i+1] = dp[i] + 1
        else:
            max_val = max(max_val, arr[i])
            dp[i+1] = dp[i]
    
    return sum(dp)

# Read input from stdin
n, K = map(int, input().split())
arr = list(map(int, input().split()))

print(count_subarrays(arr, K))
