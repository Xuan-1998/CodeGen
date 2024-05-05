def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize memoization table with all ones

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:  # If current element is greater than previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update dp[i] to be the maximum of its current value and dp[j] + 1

    return max(dp)  # The length of the longest increasing subsequence is stored in dp[n-1]
