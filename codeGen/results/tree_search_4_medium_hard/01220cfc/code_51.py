def canJump(nums):
    n = len(nums)
    dp = {i: False for i in range(n)}
    dp[n-1] = True  # Base case: last index is always reachable

    for i in range(n-2, -1, -1):  # Start from the second-to-last index
        if not dp[i]:  # If we can't reach this index
            continue
        max_reachable_index = min((i + nums[i]) if i + nums[i] < n else n-1, n-2)
        for j in range(i+1, max_reachable_index+1):
            if not dp[j]:  # If we can't reach this index
                break
        dp[i] = True  # Update the reachable status

    return dp[0]
