def maxSum(nums, k):
    dp = {}
    def dfs(i):
        if i in dp:
            return dp[i]
        if i >= len(nums) or i - k < 0:
            return (0, -1)
        res = (nums[i], i)
        for j in range(max(0, i-k), i+1):
            s, last = dfs(j)
            if last - j + k <= i - j:
                s += nums[i]
                res = max(res, (s, i))
        dp[i] = res
        return res

    _, ans = dfs(0)
    return ans

k = int(input())
nums = list(map(int, input().split()))
print(maxSum(nums, k))
