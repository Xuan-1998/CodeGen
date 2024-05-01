def num_paths_to_collect_k_coins(N, K, arr):
    memo = [[[0]*201 for _ in range(N)] for _ in range(N)]
    
    # Base case: Top-left corner
    memo[0][0][K-arr[0][0]] = 1
    
    # Fill up the dp table
    for i in range(N):
        for j in range(N):
            if i > 0:
                for k in range(201):
                    memo[i][j][k] += memo[i-1][j][max(0, k-arr[i-1][j])]
            if j > 0:
                for k in range(201):
                    memo[i][j][k] += memo[i][j-1][max(0, k-arr[i][j-1])]
    
    # Return the number of paths that collect exactly K coins
    return memo[N-1][N-1][K]
