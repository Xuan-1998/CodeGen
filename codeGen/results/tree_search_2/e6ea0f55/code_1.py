def maxSumOfSubsequence(nums, k):
    n = len(nums)
    dp = [[0]*(k+1) for _ in range(n)]
    
    for i in range(n):
        for j in range(k+1):
            if i < j:
                dp[i][j] = dp[0][j]
            elif i == 0:
                dp[i][j] = nums[i]
            else:
                max_sum = max(dp[max(0, i-k)][max_sum-k] for max_sum in range(max(1, i-k+1)))
                dp[i][j] = max_sum + nums[i]
                
    return max(dp[-1])

# Example usage
nums = list(map(int, input().split()))
k = int(input())
print(maxSumOfSubsequence(nums, k))
