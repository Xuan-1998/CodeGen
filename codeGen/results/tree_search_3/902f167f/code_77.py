def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    # Base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    memo = {}
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # If we've reached a single row or column, use the base case
        if i == 0 or j == 0:
            result = max(i, j)
        else:
            result = min(dfs(i-1, j), dfs(i, j-1)) + 1
        
        memo[(i, j)] = result
        return result
    
    return dfs(n, m)

import sys

n, m = map(int, input().split())
print(min_squares(n, m))
