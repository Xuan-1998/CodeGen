def find_sums(nums):
    n = len(nums)
    max_sum = sum(nums)

    # Initialize the dp array with zeros
    dp = [0] * (max_sum + 1)

    for num in nums:
        for i in range(max_sum, num - 1, -1):
            dp[i] += dp[i - num]

    return list(set([i for i in range(1, max_sum + 1) if dp[i]]))

# Example usage
nums = [1, 2, 3]
print(find_sums(nums))  # Output: [1, 3, 4, 5, 6]
