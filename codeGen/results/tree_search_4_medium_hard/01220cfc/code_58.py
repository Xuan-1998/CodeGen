def canJump(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True

    for i in range(1, n):
        if dp[i - 1]:
            j = min(i + nums[i], n - 1)
            while j >= 0:
                if j == n - 1:
                    return True
                if not dp[j]:
                    break
                j -= 1
            dp[i] = True

    return dp[-1]
