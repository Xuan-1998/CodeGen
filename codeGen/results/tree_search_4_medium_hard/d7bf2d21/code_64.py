def findLengthOfLIS(nums):
    n = len(nums)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(0, n + 1):
        dp[i][i] = True
        
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][i-1]
    
    max_length = 0
    for j in range(n):
        if dp[n-1][j]:
            max_length = max(max_length, j + 1)
            
    return len(set([x+1 for x in range(n) if dp[n-1][x]])) or 1

nums = list(map(int, input().split()))
print(findLengthOfLIS(nums))
