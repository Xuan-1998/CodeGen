import sys

def max_sum_of_subarrays(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(k, n + 1):
        dp[i] = max(dp[i-1], arr[i-k:i].max())

    return sum(max(subarray) for subarray in zip(*[arr[i:i+k] for i in range(0, n, k)]))

k, n = map(int, input().split())
arr = list(map(int, input().split()))
print(max_sum_of_subarrays(arr, k))
