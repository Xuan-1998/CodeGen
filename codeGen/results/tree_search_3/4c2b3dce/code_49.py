import sys

def can_form_ab_ba(s):
    dp = [[False] * (int(1e5) + 3) for _ in range(len(s) + 1)]
    dp[0][0] = True
    
    for i in range(1, len(s) + 1):
        if s[i-1] == 'A':
            dp[i][dp[i-1].index(True)].append(True)
        elif s[i-1] == 'B':
            dp[i][dp[i-2].index(True)].append(True)
        
    return any(dp[i][j] and i >= 2 for i in range(len(s), 0, -1) for j in range(int(1e5) + 3))

# Read input from stdin
s = input()

if can_form_ab_ba(s):
    print("YES")
else:
    print("NO")
