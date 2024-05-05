def isScrambled(s1, s2):
    n = len(s1)
    
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i):
            if s1[:i - j].lower() == s2[j:i].lower():
                dp[i][j] = True
                for k in range(n - i):
                    for l in range(k + 1):
                        if not dp[k + i][l + j]:
                            break
                    else:
                        if k == n - i - 1:
                            dp[i][j] = True
                            break
            else:
                for k in range(n - i):
                    for l in range(k + 1):
                        if not dp[k + i][l + j]:
                            break
                    else:
                        if k == n - i - 1:
                            dp[i][j] = False
                            break
    
    return dp[n-1][n-1]
