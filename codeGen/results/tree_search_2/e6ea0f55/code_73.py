import sys

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the base case when i = 0
    for j in range(n + 1):
        dp[0][j] = nums[j]
        
    # Fill up the DP table
    for i in range(1, n + 1):
        for j in range(i + k, -1, -1):
            for x in range(j, i + 1):
                if abs(x - j) <= k:
                    dp[i][max(dp[i-1][j], nums[x] + dp[i-x-1][j])]
                    
    # Return the maximum sum
    return max(dp[n])

nums = [int(i) for i in input().split()]
k = int(input())
print(maxSumSubsequence(nums, k))
