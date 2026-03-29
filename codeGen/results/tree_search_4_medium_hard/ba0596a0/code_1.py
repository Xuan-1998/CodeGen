def can_cross(stones):
    n = len(stones)
    dp = [[False] * (n - 1) for _ in range(n)]
    
    dp[0][0] = True
    
    for i in range(1, n):
        for j in range(max(0, i - 2), min(i + 1, n - 1)):
            if stones[j] - stones[i-1] >= 0 and (abs(stones[j] - stones[i-1]) == 1 or abs(stones[j] - stones[i-1]) == 2):
                dp[i][j % (i+1)] = True
    
    return dp[n-1][0]
