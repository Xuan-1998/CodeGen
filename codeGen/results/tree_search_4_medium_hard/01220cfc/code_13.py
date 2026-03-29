def can_jump(nums):
    n = len(nums)
    dp = [False] * (n + 1)

    for i in range(n - 1, -1, -1):
        if i == n - 1:
            dp[i] = True
        else:
            for j in range(i):
                if j + nums[j] >= i and dp[j]:
                    dp[i] = True
                    break

    return dp[-1]
