def maxSumOfSubsequence(nums, k):
    n = len(nums)
    dp = [(0, -1) for _ in range(n+1)]

    for i in range(1, n+1):
        max_sum = 0
        last_index = -1
        for j in range(max(0, i-k), i+1):
            sum, last_j_index = dp[j]
            if nums[i] + sum > max_sum:
                max_sum = nums[i] + sum
                last_index = j
        dp[i] = (max_sum, last_index)

    return dp[n][0]

# Example usage:
nums = [1, 2, 3, 4, 5]
k = 2
print(maxSumOfSubsequence(nums, k))  # Output: 9
