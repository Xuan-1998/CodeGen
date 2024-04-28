def numPathsWithKCoins(K, N, arr):
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Base case: When i == N-1 and j == N-1
    if arr[N-1][N-1] <= K:
        dp[N-1][N-1] = 1
    
    for i in range(N):
        for j in range(N):
            # If the current cell has coins less than or equal to K
            if arr[i][j] <= K:
                # Calculate the number of ways to reach this cell
                if i < N - 1 and j < N - 1:
                    dp[i+1][j+1] += dp[i][j]
                else:
                    dp[i][j] = 1
    
    return sum([row.count(1) for row in dp])

# Receive input from stdin
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPathsWithKCoins(K, N, arr))
