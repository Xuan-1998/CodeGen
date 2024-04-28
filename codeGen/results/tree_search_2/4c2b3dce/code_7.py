import sys

def check_AB_BA(s):
    m = len(s)
    dp = [[False] * 2 for _ in range(m + 1)]
    
    for i in range(m):
        if s[i:i+2] == 'AB':
            dp[i][0] = True
        elif s[i:i+2] == 'BA':
            dp[i][1] = True
        
        for j in range(2):
            if dp[i][j]:
                if j == 0:
                    for k in range(i + 2, m):
                        if s[k:k+2] != 'AB':
                            break
                        dp[k][1] = True
                else:
                    for k in range(i + 2, m):
                        if s[k:k+2] != 'BA':
                            break
                        dp[k][0] = True
    
    return "YES" if any(dp[m-1]) else "NO"

# Read input from stdin
s = sys.stdin.readline().strip()

print(check_AB_BA(s))
