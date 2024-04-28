import sys

def minUncommonLength(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return -1 if not dp[m-1][n-1] else dp[m-1][n-1]

S = input().strip()
T = input().strip()

print(minUncommonLength(S, T))
