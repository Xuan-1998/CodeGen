from collections import defaultdict

def maxSumSubsequence(nums, k):
    memo = {}
    dp = [0] * (k + 1)
    
    # Initialize the base cases
    for i in range(1, len(nums)):
        if i <= k:
            dp[i] = nums[i]
        else:
            break
    
    # Fill up the dynamic programming table
    for i in range(k, -1, -1):
        if i == 0:
            for j in range(len(nums) - 1, -1, -1):
                memo[(j, i)] = max(memo.get((j-1, i), dp[j-1]) + nums[j], nums[j])
        else:
            for j in range(max(0, i-k), len(nums)):
                if (j, i) not in memo:
                    memo[(j, i)] = max(memo.get((j-1, i-1), dp[j-1] - nums[j-1]) + nums[j], dp[j-1])
    
    # Return the maximum sum
    return max(dp)

# Test your solution
nums = list(map(int, input().split()))
k = int(input())
print(maxSumSubsequence(nums, k))
