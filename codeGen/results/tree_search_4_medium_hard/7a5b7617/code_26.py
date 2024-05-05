def solve():
    N, M = map(int, input().split())
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    # Base case: only consider the first row
    for s in range(M+1):
        dp[0][s] = 1
    
    # Fill in the dp array using dynamic programming
    for i in range(1, N+1):
        for j in range(1, M+1):
            for k in range(i):
                dp[i][j] += dp[k][M-1-k]
    
    # Return the result: total number of different steady tables
    return dp[N][M]

print(solve())
