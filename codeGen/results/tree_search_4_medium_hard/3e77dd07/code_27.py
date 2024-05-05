def isScramble(s1, s2):
    n = len(s1)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(i, n):
            if s1[i:j+1] == s2[i:j+1]:
                dp[i][j] = True
            else:
                for k in range(j):
                    if s1[i:j+1] == s2[k:k+n-j]:
                        if (k + j >= i) and dp[i][k+j-1] and dp[k+j][j]:
                            dp[i][j] = True
                            break
    
    return dp[0][n-1]

# Read input from stdin
s1, s2 = input().split()
print(isScramble(s1, s2))
