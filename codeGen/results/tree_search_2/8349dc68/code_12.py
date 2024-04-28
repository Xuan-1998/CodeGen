import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    max_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        if i < k:
            max_sum[i] = sum(arr[:i])
        else:
            max_sum[i] = max(max_sum[i-1], sum(arr[i-k+1:i+1]))

    return max_sum[-1]

# Read input from stdin
arr = list(map(int, input().split()))
k = int(input())

print(max_sum_after_partitioning(arr, k))
