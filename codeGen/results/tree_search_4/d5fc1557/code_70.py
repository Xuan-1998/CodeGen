def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize DP table with zeros

    max_length = 0
    for i in range(n):
        if nums[i] == 1:  # If the current element is 1
            dp[i + 1] = dp[i] + 1  # Update DP table accordingly
            max_length = max(max_length, dp[i + 1])  # Keep track of the maximum length
        else:
            if i > 0 and nums[i - 1] == 1:  # If the previous element is 1 (i.e., we can delete it)
                dp[i + 1] = max(dp[i], dp[i - 1])  # Update DP table accordingly
            else:
                dp[i + 1] = 0  # Reset the DP table if we encounter a 0 and no previous 1 to delete

    return max_length
