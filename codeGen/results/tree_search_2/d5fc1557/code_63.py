def longest_subarray(nums):
    n = len(nums)
    max_len = 0
    current_streak = 0
    
    dp = [0] * (n + 1) # Initialize the dp array with zeros, where dp[i] is the length of the longest subarray ending at index i

    for i in range(n):
        if nums[i] == 1:
            current_streak += 1
            dp[i + 1] = max(dp[i], current_streak)
        else:
            if current_streak > 0: # If we've seen a streak of ones, update the maximum length and reset the current streak
                max_len = max(max_len, current_streak)
                current_streak = 0

    return max(max_len, current_streak) - 1 # Return the maximum length minus one (since we need to remove one element from the array)

import sys
input_nums = [int(x) for x in input().split()]
print(longest_subarray(input_nums))
