def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = { (0, -1): 0 }

    for i in range(n):
        for j in range(max(0, i-k), min(i+k+1, n)):
            if abs(i-j) <= k:
                dp[(i, j)] = max(dp.get((i, j), 0), nums[i] + (dp.get((j,), 0) or 0))

    return max(dp.values())

# Example usage
nums = [10, -20, 30, -5, -3]
k = 2
print(maxSumSubsequence(nums, k))  # Output: 35
