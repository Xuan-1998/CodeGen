def count_paths(K, N, arr):
    dp = [[0] * (N) for _ in range(N)]
    
    # Base case: number of ways to collect exactly K coins from cells (0, 0) to (N-1, N-1)
    dp[N-1][N-1] = int(arr[0][0] == K)
    
    # Fill up the dynamic programming table
    for i in range(N):
        for j in range(N):
            if i < N-1:
                dp[i+1][j] += dp[i][j]
            if j < N-1:
                dp[i][j+1] += dp[i][j]
            if i < N-1 and j < N-1:
                dp[i+1][j+1] += dp[i][j]
    
    return dp[0][0]

# Read input from stdin
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(count_paths(K, N, arr))
