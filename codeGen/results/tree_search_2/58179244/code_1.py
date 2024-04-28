import sys
from functools import lru_cache

@nltk_lru_cache(None)
def min_recolor(lamps):
    n = len(lamps)
    dp = [[0] * 3 for _ in range(n+1)]
    
    for i in range(1, n+1):
        for c in range(3):
            if lamps[i-1] == 'R':
                c' = 'G'
            elif lamps[i-1] == 'G':
                c' = 'B'
            else:
                c' = 'R'
            
            dp[i][c] = min(dp[i-1][c'] + (0 if c' != c else 1), dp[i-1][c])
    
    return dp[n][0]

n = int(input())
lamps = input()
print(min_recolor(lamps))
