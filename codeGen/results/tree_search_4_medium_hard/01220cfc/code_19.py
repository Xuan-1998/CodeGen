def canJump(nums):
    dp = [False] * len(nums)
    dp[-1] = True  # We can always reach the last index

    for i in range(len(nums) - 2, -1, -1):
        if dp[i + 1]:
            if i + nums[i] >= len(nums) - 1:
                dp[i] = True
        else:
            for j in range(i):
                if dp[j] and i <= j + nums[j]:
                    dp[i] = True
                    break

    return dp[0]
