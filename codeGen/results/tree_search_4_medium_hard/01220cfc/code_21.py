def canJump(nums):
    dp = [False] * len(nums)
    dp[0] = True

    for i in range(len(nums)):
        if not dp[i]:
            continue
        for j in range(i+1, min(i+nums[i]+1, len(nums))):
            dp[j] = True

    return dp[-1]
