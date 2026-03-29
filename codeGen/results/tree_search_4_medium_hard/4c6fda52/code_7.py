import sys

def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for i in range(k + 1):
        dp[0][i] = i
    
    for i in range(1, n + 1):
        for c in range(k + 1):
            if s[i - 1] == 'R':
                dp[i][c] = min(dp[i - 1][c], dp[i - 1][c - 1] + (s[i - k:i].count('G') > 0 or s[i - k:i].count('B') > 0))
            else:
                dp[i][c] = min(dp[i - 1][c], dp[i - 1][c - 1] + (s[i - k:i].count('R') == 0 and s[i - k:i].count('G') > 0) or (s[i - k:i].count('R') == 0 and s[i - k:i].count('B') > 0))
    
    return min(dp[n][k], n)

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

print(min_changes(s, k))
