from collections import defaultdict

def count_bear_pairs(s):
    n = len(s)
    bear = 'bear'
    
    dp = [defaultdict(int) for _ in range(n + 1)]
    for i, c in enumerate(s):
        dp[i + 1][c] += 1
    
    res = 0
    for i, c in enumerate(s):
        for j in range(i + len(bear)):
            if s[j:j+len(bear)] == bear and all(dp[k][c] >= 1 for k in range(i, j+1)):
                res += 1
    
    return res

# Receive input from stdin
s = input()

# Print the result to stdout
print(count_bear_pairs(s))
