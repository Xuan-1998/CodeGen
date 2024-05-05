from collections import defaultdict

def canJump(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True
    
    for i in range(1, n):
        if not dp[i]:
            for j in range(i):
                if j <= i and nums[j] >= i - j:
                    dp[i] = True
                    break
    
    return dp[-1]

# Example usage:
nums = [2,3,1,1,4]
print(canJump(nums))  # Output: True

