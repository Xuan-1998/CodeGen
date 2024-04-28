def longest_subarray(nums):
    n = len(nums)
    dp = [[0] * 2 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0]) + 1
        else:
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

    return max(max(row) for row in dp)

# Example usage
nums = [1, 1, 0, 1, 1, 1]
print(longest_subarray(nums))  # Output: 4
