import sys

def min_operations(arr):
    n = len(arr)
    max_val = max(arr)
    dp = [float('inf')] * (max_val + 1)

    for i in range(n):
        for j in range(min(arr[i], max_val), -1, -1):
            if arr[i] > j:
                dp[j] = min(dp[j], dp[arr[i]] + 1)
    return dp[max_val]

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
