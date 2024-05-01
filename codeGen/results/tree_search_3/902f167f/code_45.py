import sys
from collections import namedtuple

# Define the state as (n, m) where n represents the remaining row height and m represents the remaining column width.
State = namedtuple('State', 'n m')

def solve():
    n, m = map(int, input().split())
    
    # Initialize dp with infinity or some large value
    dp = [[sys.maxsize] * (m + 1) for _ in range(n + 1)]
    
    # Base case: when the remaining rectangle has a size of 0x0.
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the remaining rectangle can be fully covered by a square, update the state
            if i >= j:
                dp[i][j] = min(dp[i][j], dp[i - j][0] + (i // j) ** 2)
            else:
                # Update the state when a square is placed at the bottom or right edge of the rectangle.
                dp[i][j] = min(dp[i][j], dp[0][j - 1] + (i + 1) ** 2)
    
    return dp[n][m]

print(solve())
