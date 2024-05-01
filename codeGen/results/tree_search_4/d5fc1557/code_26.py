from collections import defaultdict

def maximum_ones(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize dynamic programming table
    max_length = 0

    memo = defaultdict(int)

    for i in range(n):
        if nums[i] == 1:
            dp[i + 1] = max(dp[i], max_length + 1)
            max_length = max_length + 1 if max_length > 0 else 1
        else:
            dp[i + 1] = max(dp[i], 0)

    return max(0, max(dp) - 1)  # Return the maximum length minus 1

# Example usage
nums = [0, 1, 0, 1, 0, 1]
print(maximum_ones(nums))  # Output: 2
