def canJump(nums):
    n = len(nums)
    dp = [[False] * 2 for _ in range(n)]

    dp[0][1] = True
    for i in range(1, n):
        for j in range(i):
            if nums[j] >= i - j and dp[j][1]:
                dp[i][1] = True
                break

    return dp[n-1][1]
