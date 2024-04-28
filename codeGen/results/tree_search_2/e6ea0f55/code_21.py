import sys

def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Initialize the base cases
    dp[0][0] = nums[0]
    
    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], nums[i])
            else:
                # Consider including and excluding the current element
                include = nums[i] + dp[i-1][j-1]
                exclude = dp[i-1][j]
                dp[i][j] = max(include, exclude)
    
    return max(dp[-1])

# Example usage
nums = list(map(int, input().split()))
k = int(input())
print(max_sum_subsequence(nums, k))
