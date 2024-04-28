def longest_ones_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # dp[i] represents the max length of consecutive ones ending at i

    max_length = 0
    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = max(dp[i-1], 0)
        max_length = max(max_length, dp[i])

    return max_length - 1  # subtract 1 because we removed one element

# Example usage:
import sys
n = int(sys.stdin.readline())
nums = [int(x) for x in sys.stdin.readline().split()]
print(longest_ones_subarray(nums))
