def longest_subarray(nums):
    n = len(nums)
    max_length = 0
    prefix_sum = [0]
    
    for num in nums:
        if num == 1:
            prefix_sum.append(prefix_sum[-1] + 1)
        else:
            prefix_sum.append(0)

    dp = [0] * (n + 1)
    dp[0] = n
    max_length = 0

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = max(dp[i], dp[i - 1] + 1)
        else:
            dp[i] = max(dp[i], dp[i - 1] - 1)

    for i in range(n + 1):
        max_length = max(max_length, dp[i])

    return n - max_length
