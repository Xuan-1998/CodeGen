def find_length_of_longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP with ones (subsequences of length 1)
    memo = {}  # Memo dictionary to store previously computed results

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:  # If current element is greater than previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update DP[i] with the maximum length
        memo[i] = dp[i]  # Store computed values in memo dictionary

    return max(memo.values())  # Return the maximum value (number of longest subsequences)
