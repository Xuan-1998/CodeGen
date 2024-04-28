import sys

def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k+1) for _ in range(n)]
    
    # Base case: when i = 0
    for j in range(k+1):
        dp[0][j] = nums[0]
    
    for i in range(1, n):
        for j in range(min(i, k)+1):
            # Including the current element
            include = dp[i-1][min(j+1, k)] + nums[i]
            # Excluding the current element
            exclude = dp[i-1][j]
            dp[i][j] = max(include, exclude)
    
    return max(dp[-1])

# Input: Read from standard input
nums = list(map(int, input().split()))
k = int(input())

print(max_sum_subsequence(nums, k))
