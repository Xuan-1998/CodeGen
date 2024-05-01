import sys

def solve():
    s = input().strip()
    dp = [[False, False]] * (len(s) + 1)
    
    for i in range(1, len(s) + 1):
        if s[i - 1] == 'A':
            dp[i][0] = dp[i - 1][1]
        elif s[i - 1] == 'B' and dp[i - 1][0]:
            dp[i][1] = True
    
    return "YES" if any(dp[-1]) else "NO"

print(solve())
