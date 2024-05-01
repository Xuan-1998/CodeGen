def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize DP array with zeros

    for i in range(1, n):  # Iterate over the array
        max_length = 0   # Initialize maximum length found so far
        j = i - 1   # Initialize j as the last 1 before deletion
        while j >= 0 and nums[j] == 1:   # Move backwards until we find a 0 or reach the start
            max_length = max(max_length, i - j)   # Update maximum length found so far
            j -= 1   # Move one step back
        dp[i + 1] = max(dp[i], max_length) if nums[i] == 1 else dp[i]   # Update the dynamic programming table

    max_length = 0
    for i in range(n - 2, -1, -1):   # Iterate over the array backwards
        if nums[i] == 1:   # If we find a 1
            max_length = dp[i + 1]   # Update maximum length found so far
            break

    return max_length if max_length > 0 else 0   # Return the maximum length or 0 if no such subarray exists
