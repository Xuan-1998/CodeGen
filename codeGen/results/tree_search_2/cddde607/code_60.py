def findPaths(K, N, arr):
    dp = [[False for _ in range(N)] for _ in range(N)]
    
    # Base case: It's always possible to reach the top-left cell with 0 coins.
    dp[0][0] = True
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= K:
                if (i == N-1 and j < N-1) or (j == N-1 and i < N-1):
                    dp[i][j] = dp[i][j] or (dp[i+1][j] if i < N-1 else False) or (dp[i][j+1] if j < N-1 else False)
                if i < N-1:
                    dp[i+1][j] = dp[i+1][j] or (dp[i][j] and arr[i][j] <= K - arr[i+1][j])
                if j < N-1:
                    dp[i][j+1] = dp[i][j+1] or (dp[i][j] and arr[i][j] <= K - arr[i][j+1])
    
    # Count the number of paths that collect exactly K coins.
    return sum(1 for i in range(N) if dp[N-1][i])

# Receive inputs from stdin
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(findPaths(K, N, arr))
