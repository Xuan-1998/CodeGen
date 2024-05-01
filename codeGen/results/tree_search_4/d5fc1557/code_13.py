def longest_subarray(nums):
    n = len(nums)
    dp = {0: 0}  # initialize the DP dictionary

    for i in range(1, n):
        if nums[i] == 1:
            dp[i] = max(dp.get(i-1, 0) + 1, 0)
        else:
            dp[i] = max(0, dp.get(i-1, 0))

    # handle edge cases
    if all(x == 1 for x in nums):
        return n
    elif all(x == 0 for x in nums):
        return 0

    # find the maximum length of subarray containing only 1's
    max_length = max(dp.values())

    return max_length
