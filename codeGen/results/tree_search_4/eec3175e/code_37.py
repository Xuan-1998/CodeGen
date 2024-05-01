def find_subset(n, m, nums):
    dp = [[False] * m for _ in range(n+1)]
    
    for i in range(n+1):
        if i == 0:
            dp[i][0] = True
        elif i > 0 and nums[i-1] <= m:
            dp[i][nums[i-1]%m] = True
            
            for j in range(i):
                if i >= j + 1 and (i-j-1)%m == (nums[j]%m):
                    dp[i][(nums[i-1]+nums[j])%m] = dp[i-j-1][j]%m or dp[i][nums[i-1]%m]
                    
    for k in range(m):
        if dp[n][k]:
            return 1
    return 0

