def canJump(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True

    for i from 1 to n:
        if arr[i] >= 1 and dp[i-arr[i]]:
            dp[i] = True
        elif i > 0:
            dp[i] = dp[i-1]

    return dp[n-1]
