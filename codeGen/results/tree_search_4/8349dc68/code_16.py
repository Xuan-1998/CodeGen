from collections import deque

def max_sum(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        window_max = max(arr[i - k:i])
        if i >= k:
            window_max = max(window_max, arr[i - k:i][0])
        dp[i] = max(dp[i - 1] + window_max, 0)

    return max(dp)
