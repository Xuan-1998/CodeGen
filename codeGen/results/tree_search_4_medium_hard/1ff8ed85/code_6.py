import sys
from collections import defaultdict

# Read number of test cases
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    # Initialize dp table
    dp = [[False] * (10**9 + 1) for _ in range(n + 1)]
    prev_val = float('-inf')
    for i in range(1, n + 1):
        for j in range(b[i - 1], 10**9 + 1):
            if b[i - 1] <= j:
                dp[i][j] = or_(dp[i - 1][k] for k in range(j))
            else:
                dp[i][j] = dp[prev_val][j]
        prev_val = i
    
    # Print result
    print('YES' if dp[n][b[-1]] else 'NO')
