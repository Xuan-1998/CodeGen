import sys

def canJump(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True
    
    for i in range(1, n):
        for j in range(i):
            if dp[j]:
                if j + nums[j] >= i:
                    dp[i] = True
                    break
        else:
            dp[i] = False
    
    return dp[-1]

input_nums = list(map(int, input().split()))
print(canJump(input_nums))
