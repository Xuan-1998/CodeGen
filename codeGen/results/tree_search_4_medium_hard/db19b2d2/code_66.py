import sys
from collections import defaultdict

def prob_at_least_one_player(n, m, h, s):
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize dp[0][j] to 0 for all j, because there's no team formed with 0 players.
    for j in range(m + 1):
        dp[0][j] = 0.0
    
    # Calculate the probability that a team of size i will have at least one player from the department of interest.
    for i in range(1, n + 1):
        if s[h - 1] >= i:
            dp[i][h - 1] = 1.0
        else:
            dp[i][h - 1] = (s[h - 1] + dp[i - 1][h - 1]) / s[h - 1]
        
        for j in range(m):
            if j == h - 1:
                dp[i][j] = min(1.0, (s[j] + dp[i - 1][j]) / s[j])
            else:
                dp[i][j] = max(dp[i - 1][j], 1.0 - (s[j] + dp[i - 1][h - 1]) / s[j])
    
    return dp[n][h - 1]

# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

print(prob_at_least_one_player(n, m, h, s))
