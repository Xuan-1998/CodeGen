from collections import defaultdict

def numPaths(arr):
    N = len(arr)
    K = int(input())
    
    # Initialize dp table
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    # Base case: only one way to reach top-left cell with 0 coins
    dp[0][0][0] = 1
    
    memo = defaultdict(dict)
    
    def dfs(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        
        total_paths = 0
        
        # If we're not at the edge and there are coins left
        if i < N - 1 or j < N - 1:
            # Count the number of paths that move up (if possible)
            if arr[i][j] <= k:
                total_paths += dp[i-1][j][k]
            
            # Count the number of paths that move right (if possible)
            if arr[i][j] <= k:
                total_paths += dp[i][j-1][k]
        
        memo[(i, j, k)] = total_paths
        return total_paths
    
    return dfs(N - 1, N - 1, K)

print(numPaths(list(map(int, input().split()))))
