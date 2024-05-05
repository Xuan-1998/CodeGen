def is_scrambled(s1, s2):
    if len(s1) != len(s2):
        return False
    
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    def helper(i, j):
        if i >= len(s1) or j >= len(s2):
            return True
        
        if s1[i] == s2[j]:
            dp[i][j] = True
            return True
        
        for k in range(i+1, len(s1)+1):
            for l in range(j+1, len(s2)+1):
                if helper(k-1, l-1) and is_scrambled(s1[:k], s2[:l]):
                    dp[i][j] = True
                    return True
        
        return False
    
    return helper(0, 0)
