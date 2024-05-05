import sys
from collections import defaultdict

def min_operations(n, parent, ranges):
    # Initialize the 2D table for memoization
    dp = [[0] * (10**9 + 1) for _ in range(n + 1)]
    
    # Traverse the graph in topological order
    for i in range(1, n + 1):
        if parent[i - 1] == -1:  # If this is the root node
            continue
        
        # Update the minimum number of operations for this vertex and its ancestors
        l, r = ranges[i - 1]
        dp[i][l] += dp[parent[i - 1]][l]
        dp[i][r] += dp[parent[i - 1]][r]
        
        # Apply the minimum number of operations needed to adjust the value
        for j in range(l + 1, r):
            if not dp[i][j]:
                dp[i][j] = dp[i][l] + (r - j)
    
    # Return the total minimum number of operations needed
    return sum(min(dp[i][j] for j in range(10**9)) for i in range(n + 1))

# Read input from standard input
T = int(input())
for _ in range(T):
    n = int(input())
    parent = list(map(int, input().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, input().split())
        ranges.append((l, r))
    
    # Calculate and print the minimum number of operations needed
    result = min_operations(n, parent, ranges)
    print(result)

