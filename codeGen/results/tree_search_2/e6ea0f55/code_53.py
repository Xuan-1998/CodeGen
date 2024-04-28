def maxSumSubsequence(nums, k):
    n = len(nums)
    memo = {}

    def dp(i, s):
        if (i, s) in memo:
            return memo[(i, s)]
        if i == 0:
            return s
        res = s
        for j in range(1, min(i+1, k+1)):
            res = max(res, nums[i-j] + dp(i-j, s-nums[i-j]))
        memo[(i, s)] = res
        return res

    ans = 0
    for i in range(n):
        ans = max(ans, dp(i, sum(nums[:i+1])))
    return ans
