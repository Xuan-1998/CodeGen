def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    memo = {}

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        memo[nums[i]] = dp[i]

    return max(memo.values())
