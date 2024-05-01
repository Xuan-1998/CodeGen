def longestSubarray(nums):
    n = len(nums)
    dp = [False] * (n + 1)

    # Initialize the state for index 0
    dp[0] = True if nums[0] == 1 else False

    max_length = 0

    for i in range(1, n + 1):
        if (i == 1 or nums[i - 1] == 0) and all(nums[j] == 1 for j in range(i, n)):
            dp[i] = True
            max_length = max(max_length, i)
        else:
            dp[i] = False

    # The maximum length of the subarray containing only 1's is stored at index n.
    return max_length if any(dp) else 0
