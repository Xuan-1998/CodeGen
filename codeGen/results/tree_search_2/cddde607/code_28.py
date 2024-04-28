def findPaths(K, N, arr):
    # Initialize the DP table with zeros
    dp = [[0]*N for _ in range(N)]
    
    # Initialize the memoization dictionary with None values
    memo = {(i, j): None for i in range(N) for j in range(N)}
    
    def dfs(i, j, k):
        # Base case: if we've reached the bottom right cell and have exactly K coins, return 1
        if i == N-1 and j == N-1:
            return int(k == 0)
        
        # If we've already computed this cell, return the result from memoization
        if memo[(i, j)] is not None:
            return memo[(i, j)]
        
        # Initialize the count of valid paths to 0
        count = 0
        
        # Consider all possible moves from this cell
        for di, dj in [(-1, 0), (0, -1)]:
            ni, nj = i+di, j+dj
            
            # If we can move to the new cell and have exactly K coins left, increment the count
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] + k <= K:
                count += dfs(ni, nj, k-arr[i][j])
        
        # Store the result in memoization for future use
        memo[(i, j)] = count
        
        return count
    
    # Start DFS from the top left cell with K coins
    return dfs(0, 0, K)
