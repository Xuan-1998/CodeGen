def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
nums = list(map(int, input().split()))

# Calculate the length of the longest increasing subsequence
lis_length = longest_increasing_subsequence(nums)

# Print the answer to stdout
print(lis_length)
