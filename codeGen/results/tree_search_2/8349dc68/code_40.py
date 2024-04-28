import sys
from collections import defaultdict

def max_sum(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(k - 1, -1, -1):
        dp[i] = max(dp[:i]) if i > 0 else max(arr[:i])

    max_sum = 0
    for i in range(k, n + 1):
        max_sum = max(max_sum, arr[i - k:i])
        dp[i] = max(dp[i - 1], arr[i - 1] + dp[i - k]) if i >= k else max(arr[:i])

    return max_sum

k = int(input())
arr = list(map(int, input().split()))
print(max_sum(arr, k))
