import sys

def max_subsequence_sum(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)

    # Base case: maximum sum is simply the maximum element in nums
    dp[0] = max(nums)

    for i in range(1, n + 1):
        if i <= k:
            dp[i] = max(dp[i-1], nums[i-1])
        else:
            max_sum = -float('inf')
            for j in range(max(0, i-k), i):
                max_sum = max(max_sum, dp[j] + nums[i-1])
            dp[i] = max_sum

    return dp[-1]

# Example usage
nums = [1, 2, 3, 4, 5]
k = 2
print(max_subsequence_sum(nums, k))  # Output: 9
