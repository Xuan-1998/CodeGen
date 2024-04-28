def max_sum_of_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: dp[0][j] = nums[0] for j in range(k+1)
    dp[0][0] = nums[0]

    for i in range(1, n):
        for j in range(min(i, k)+1):
            if j == 0:
                # No restriction on the previous element
                dp[i][j] = max(dp[i-1][j] + nums[i], dp[0][0] + nums[i])
            else:
                # Consider all possible choices for the previous element
                dp[i][j] = max(dp[i-1][min(j-1, k)+1] + nums[i], dp[i-k-1][j] + nums[i])

    return max(dp[-1])

# Example usage:
nums = [4, 2, 9, 3]
k = 2
print(max_sum_of_subsequence(nums, k))  # Output: 12 (subsequence: [4, 9])
