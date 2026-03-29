### BEGIN CODE ###

import sys
from collections import defaultdict

# Read input and initialize variables
n = int(input())
tickets = [int(line) for line in (sys.stdin.readlines())]

# Initialize dynamic programming table
dp = [[float('inf') for _ in range(100)] for _ in range(n+1)]
dp[0][0] = 0

for i, t in enumerate(tickets):
    for k in range(min((t+59)//90, 99)):
        if dp[i-1][k]:
            dp[i][k] = min(dp[i-1][k], dp[i-1][k//3]*2 + (1-k//3)*20)
        else:
            dp[i][k] = float('inf')
    for k in range(100):
        if dp[i][k]:
            dp[i+1][k] = min(dp[i+1][k], dp[i][k])
        else:
            dp[i+1][k] = float('inf')

# Print output
for i, t in enumerate(tickets[1:], 1):
    print(min((dp[i-1][k]+50) for k in range((t+59)//90, min((t+59)//90, 99))))

### END CODE ###
