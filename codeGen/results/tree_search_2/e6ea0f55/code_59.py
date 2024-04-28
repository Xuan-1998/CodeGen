def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = {}

    def dfs(i, prev_index):
        if (i, prev_index) in dp:
            return dp[(i, prev_index)]
        if i < 0 or i >= n or prev_index < 0:
            return 0
        res = nums[i]
        for j in range(prev_index+1, min(prev_index+k+1, n)):
            res = max(res, dfs(j-1, j-i) + nums[i])
        dp[(i, prev_index)] = res
        return res

    return max(dfs(i, -1) for i in range(n))
