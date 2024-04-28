def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # dp[i] is the maximum length of consecutive ones ending at i

    max_length = 0
    for i in range(1, n + 1):  # start from 1 to avoid overwriting dp[0]
        if nums[i - 1] == 1:  # current element is 1
            dp[i] = dp[i - 1] + 1
        else:  # current element is 0
            dp[i] = 0

        max_length = max(max_length, dp[i])

    return max_length - 1  # subtract 1 to account for the removed element

# Example usage:
nums = [1, 1, 0, 1, 1]
print(longest_subarray(nums))  # Output: 3
