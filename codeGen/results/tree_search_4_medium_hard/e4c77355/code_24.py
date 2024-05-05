def longest_increasing_subsequence(arr):
    n = len(arr)
    
    # Handle edge cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [1] * n  # Store the length of the longest increasing subsequence ending at each position
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
