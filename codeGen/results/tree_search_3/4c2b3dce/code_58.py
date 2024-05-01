import sys

def check_AB_BA(s):
    n = len(s)
    
    # Initialize dp array
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(n):
        if s[i:i+2] == 'AB':
            dp[i+2] = dp[i] or dp[i+2]
        elif s[i:i+2] == 'BA':
            dp[i+2] = dp[i] and dp[i+1]
    
    return "YES" if dp[-1] else "NO"

# Read input from stdin
s = sys.stdin.readline().strip()

print(check_AB_BA(s))
