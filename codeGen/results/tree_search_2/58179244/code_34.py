import sys
from collections import defaultdict

def solve():
    n = int(input())
    s = input()
    
    # Initialize the dynamic programming table with False values
    dp = [[False] * 3 for _ in range(n + 1)]
    
    # Base case: a garland of length 0 is always diverse
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(3):  # 0 for R, 1 for G, 2 for B
            if s[i - 1] == 'R' and j == 0:
                dp[i][j] = True
            elif s[i - 1] == 'G' and j == 1:
                dp[i][j] = True
            elif s[i - 1] == 'B' and j == 2:
                dp[i][j] = True
            
            # If the current color is not the same as the last color, 
            # we can safely assume that the garland up to this point is diverse
            if i > 0 and (dp[i - 1].index(s[i - 1]) != j):
                dp[i][j] = True
    
    r = 0
    t = ''
    
    for i in range(n, 0, -1):
        for j in range(3):
            if dp[i][j]:
                t += {'R': 'G', 'G': 'B', 'B': 'R'}[s[i - 1]]
                r += 1
                break
    
    print(r)
    print(t[::-1])

if __name__ == "__main__":
    solve()
