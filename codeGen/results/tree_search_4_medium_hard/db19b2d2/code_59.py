import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [[0.0 for _ in range(m+1)] for _ in range(n+1)]
    
    if sum(s) < n:
        return -1
    
    for i in range(1, n+1):
        for j in range(1, min(i, m)+1):
            if s[h-1] >= 1 and i == h:
                dp[i][j] = (s[h-1] / sum(s)) + dp[i-1][j]
            else:
                dp[i][j] = 1 - dp[i-1][j-1]
    
    return dp[n][m]

print(format(solve(), '.6f'))
