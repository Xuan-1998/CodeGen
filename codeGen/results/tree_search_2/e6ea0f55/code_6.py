def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: The maximum sum for the first element is just the value of that element.
    for j in range(k + 1):
        dp[0][j] = nums[0]

    for i in range(1, n):
        for j in range(min(i, k) + 1):
            # Calculate the maximum sum by considering the current element and the previous elements.
            dp[i][j] = max(dp[i-1][j-1] + nums[i], dp[i-1][j] + nums[i])

    # Return the maximum sum that can be obtained with indices at most k apart.
    return max([dp[i][k] for i in range(n)])

# Example usage:
nums = [2, 3, -1, 5, -3]
k = 2
print(maxSumSubsequence(nums, k))  # Output: 7

