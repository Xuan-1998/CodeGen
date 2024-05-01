def max_sum_after_partitioning(arr, k):
    n = len(arr)
    if n <= k:
        return sum(arr)

    dp = [0] * (n + 1)
    max_val = arr[0]
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], max_val)
        max_val = max(max_val, arr[i])

    return sum([min(k, i) * dp[i] for i in range(n)])

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, (input().split())))

print(max_sum_after_partitioning(arr, k))
