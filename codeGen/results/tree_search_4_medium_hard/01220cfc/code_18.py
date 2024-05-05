def canJump(candidates):
    dp = [False] * len(candidates)
    dp[0] = True
    
    for i in range(1, len(candidates)):
        for j in range(i):
            if dp[j]:
                if j + candidates[j] >= i:
                    dp[i] = True
                    break
                    
    return dp[-1]
