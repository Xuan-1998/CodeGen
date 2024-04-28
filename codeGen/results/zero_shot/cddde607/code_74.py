def solve():
    K, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # Initialize a 3D DP table with zeros
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    # Base case: When we are at the top left corner and K is zero, there's one path.
    dp[0][0][0] = 1
    
    # Fill up the DP table
    for i in range(N):
        for j in range(N):
            if i > 0:
                dp[i][j][:] = [x + y for x, y in zip(dp[i-1][j], dp[i][j])]
            if j > 0:
                dp[i][j][:] = [x + y for x, y in zip(dp[i][j], dp[i][j-1])]
    
    # Count the number of paths that collect exactly K coins
    return sum(1 for path in dp[N-1][N-1] if path == K)

print(solve())
