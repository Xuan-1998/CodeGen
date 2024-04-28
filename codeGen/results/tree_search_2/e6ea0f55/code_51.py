def maxSumSubsequence(nums, k):
    n = len(nums)
    memo = {}

    def dp(i, sum):
        if (i, sum) in memo:
            return memo[(i, sum)]
        
        if i > n or sum < 0:
            return float('-inf')

        max_sum = max(dp(i-1, nums[i] + sum), dp(max(0, i-k), sum))
        memo[(i, sum)] = max_sum
        return max_sum

    return dp(n-1, 0)
