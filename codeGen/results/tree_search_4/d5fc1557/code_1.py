def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = max(dp[i - 1] - 1, 0)

    return max(dp) if max(dp) > 0 else 0

n = int(input())
nums = [int(x) for x in input().split()]
print(longest_subarray(nums))
