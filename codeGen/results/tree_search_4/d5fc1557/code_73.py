def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # dp[i] is the maximum length of subarray ending at i

    for i in range(1, n + 1):  # iterate through the array
        if nums[i - 1]:  # current element is 1
            dp[i] = dp[i - 1] + 1  # update dp[i] by adding 1 to the previous cell's value
        else:  # current element is 0
            dp[i] = max(dp[i - 1], dp[i - 2] + 1) if i > 1 else 0  # decide whether to include or exclude the current element

    return dp[n]
