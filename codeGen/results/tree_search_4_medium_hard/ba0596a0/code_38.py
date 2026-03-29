def canCross(stones):
    n = len(stones)
    dp = {0: True}
    
    for j in range(1, n):
        if stones[j] - stones[j-1] <= 2:
            dp[j] = False
        else:
            for k in range(max(-1, stones[j]-stones[j-1]-3), min(n-1, stones[j]-stones[j-1]+4)):
                if k-1 >= 0 and dp.get(k-1, False):
                    dp[j] = True
                    break
            else:
                dp[j] = False
    
    return dp[n-1]
