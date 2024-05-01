def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # initialize dp array with zeros

    for i in range(1, n + 1):
        if nums[i - 1] == 1:  # if current element is '1'
            dp[i] = max(dp[i], dp[i - 1] + 1)  # update dp array
        else:
            dp[i] = 0  # reset count

    return max(dp)
