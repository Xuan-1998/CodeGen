from functools import reduce

def solve(s):
    dp = [[False] * 2 for _ in range(len(s) + 1)]
    
    for i in range(1, len(s) + 1):
        if s[i - 1] == 'A':
            dp[i][0] = dp[i - 1][0] or (i >= 2 and s[i - 2:i] == 'BA')
            dp[i][1] = dp[i - 1][1] or (i >= 2 and s[i - 2:i] == 'AB')
        elif s[i - 1] == 'B':
            dp[i][0] = dp[i - 1][0] or (i >= 2 and s[i - 2:i] == 'BA')
            dp[i][1] = dp[i - 1][1] or (i >= 2 and s[i - 2:i] == 'AB')
        else:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
    
    is_ab = any(dp[-1])
    is_ba = all(not x for x in dp[-1])
    return 'YES' if is_ab and is_ba else 'NO'

# Read input from stdin
s = input().strip()

# Print the output to stdout
print(solve(s))
