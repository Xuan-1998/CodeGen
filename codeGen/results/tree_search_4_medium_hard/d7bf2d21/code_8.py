from collections import defaultdict

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    longest_len = max(dp)
    return sum(1 for x in dp if x == longest_len)
