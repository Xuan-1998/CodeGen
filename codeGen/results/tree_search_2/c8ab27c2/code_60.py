def findLength(S, T):
    m, n = len(S), len(T)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 0
            elif S[i-1] != T[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = 1 + dp[i-1][j-1]
                
    return dp[m][n]

S = input()
T = input()

print(findLength(S, T))
