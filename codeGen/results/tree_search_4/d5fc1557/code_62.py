def longest_subarray(nums):
    n = len(nums)
    if n == 0:  # edge case: empty array
        return 0

    dp = [0] * (n + 1)  # initialize dynamic programming table
    max_length = 0

    for i in range(n):
        if nums[i] == 1 and (i == 0 or nums[i - 1] == 1):  # check if current num is 1 and prev num is also 1
            dp[i + 1] = dp[i] + 1
        else:
            dp[i + 1] = dp[i]

        max_length = max(max_length, dp[i + 1])

    return max_length - 1  # subtract 1 because we included the last element in the computation
