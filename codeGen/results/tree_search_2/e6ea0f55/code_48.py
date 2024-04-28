def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0, -1] for _ in range(n)]
    
    def dfs(i):
        if i > 0:
            return dp[i][0], dp[i][1]
        
        for j in range(min(i+k+1, n)):
            if j == 0 or i-j <= k and nums[j] + nums[i] - nums[dp[j-1][1]] > dp[j-1][0]:
                dp[j] = [nums[j] + nums[i], i]
        return dp[-1][0], dp[-1][1]
    
    _, last_index = dfs(n-1)
    return sum(nums[last_index:i+1] for i in range(last_index+k, -1, -1))

# Example usage:
k = int(input())
nums = list(map(int, input().split()))
print(maxSumSubsequence(nums, k))
