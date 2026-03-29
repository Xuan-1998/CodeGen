import sys

def min_cuts(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            if s[j-1:i].lower() == s[j-1:i].lower()[::-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][k]+1 for k in range(j, i))
    
    return dp[n][0]

s = input().strip()
print(min_cuts(s))
