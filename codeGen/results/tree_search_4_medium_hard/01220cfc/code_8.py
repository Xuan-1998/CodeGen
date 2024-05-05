def canJump(nums):
    n = len(nums)
    dp = [False] * n

    # Base case: We can always reach the first element (it has no previous elements to jump from).
    dp[0] = True

    for i in range(1, n):
        for j in range(i):
            if j <= nums[j] and dp[j]:
                dp[i] = True
                break

    return dp[-1]
