def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize the dynamic programming table
    
    max_length = 0  # Variable to store the maximum length of the subarray
    
    for i in range(1, n + 1):  # Iterate through the array
        if nums[i - 1] == 1:  # If the current element is 1
            dp[i] = dp[i - 1] + 1  # Update the dynamic programming table accordingly
            max_length = max(max_length, dp[i])  # Update the maximum length
    
    return max_length if max_length > 0 else 0  # Return the maximum length or 0 if no such subarray exists

# Example usage:
nums = [1, 1, 0, 1]
print(longestSubarray(nums))  # Output: 3
