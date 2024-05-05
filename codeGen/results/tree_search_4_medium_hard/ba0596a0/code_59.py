def canCrossStones(stones):
    n = len(stones)
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    # Base case: start on the first stone with distance 0
    dp[0][0] = 0
    
    for i in range(1, n):
        for d in range(max(1, stones[i] - stones[i-1]), min(k+1, stones[i]-stones[i-2])):
            if dp[i-1][d-1] != float('inf'):
                dp[i][d] = min(dp[i][d], dp[i-1][d-1] + 1)
    
    return dp[-1][-1] != float('inf')
