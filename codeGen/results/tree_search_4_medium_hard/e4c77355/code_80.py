def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage:
nums = list(map(int, input().split()))
print(longest_increasing_subsequence(nums))
