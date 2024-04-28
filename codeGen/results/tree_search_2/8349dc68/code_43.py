import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = {}
    for i in range(n):
        if i < k:
            dp[i] = max(0, *arr[:i+1])
        else:
            last_k_elements = arr[i-k+1:i+1]
            dp[i] = dp.get(i-1, 0) + max(0, *last_k_elements)
    return max(dp.values())

# Read input from standard input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Calculate and print the maximum sum after partitioning
print(max_sum_after_partitioning(arr, k))
