import sys

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Initialize base case when k = 0
    for i in range(n):
        dp[i][0] = nums[i]
    
    # Calculate maximum sum of subsequences ending at index j where |i-j| <= k, and consider the element at index i
    for i in range(1, n):
        for d in range(min(i, k) + 1):
            if i - d >= 0:
                dp[i][d] = max(dp[i-1][d], dp[i-1][min(d-1, i-d-1)] + nums[i])
    
    # Return the maximum sum of a non-empty subsequence
    return max(max(row) for row in dp)

# Input from stdin
nums = list(map(int, input().split()))
k = int(input())

print(maxSumSubsequence(nums, k))
