def canJump(nums):
    n = len(nums)
    dp = [[False] * n for _ in range(2)]
    
    # Base case: initialize the first index as reachable
    dp[0][0] = True
    
    for i in range(n):
        if not dp[0][i]:
            continue
        
        for j in range(i+1, min(i+nums[i]+1, n)):
            dp[1][j] = True
    
    return dp[1][-1]

# Test the function
input_nums = list(map(int, input().split()))
print(canJump(input_nums))
