def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if arr[i - 1] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
