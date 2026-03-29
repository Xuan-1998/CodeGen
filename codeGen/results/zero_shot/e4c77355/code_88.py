def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)  # Initialize DP array with length 1 sequences
    max_length = 1  # Initialize maximum length

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:  # Check if current num is greater than previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update DP array with new maximum length
        max_length = max(max_length, dp[i])  # Keep track of the maximum length

    return max_length

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    print(longest_increasing_subsequence(nums))
