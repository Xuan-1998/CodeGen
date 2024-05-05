def lengthOfLIS(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp table with all 1's

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
