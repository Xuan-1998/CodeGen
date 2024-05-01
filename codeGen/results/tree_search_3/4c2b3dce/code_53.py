import sys

def check_abba(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize start state
    if s[0] == 'A' and s[1] == 'B':
        dp[0][1] = True
    elif s[0] == 'B' and s[1] == 'A':
        dp[0][1] = True
    
    for i in range(2, n):
        if s[i-1] == 'A' and s[i] == 'B':
            for j in range(i-1, -1, -1):
                if s[j] == 'B' and s[j+1] == 'A':
                    dp[j][i] = True
                    break
        elif s[i-1] == 'B' and s[i] == 'A':
            for j in range(i-1, -1, -1):
                if s[j] == 'A' and s[j+1] == 'B':
                    dp[j][i] = True
                    break
    
    # Check the last state of DP array
    for i in range(n):
        if dp[i][n-1]:
            return "YES"
    
    return "NO"

s = input()
print(check_abba(s))
