def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case
    for i in range(1, N + 1):
        dp[i][1] = 2  # Only two choices for a single column
    for j in range(1, M + 1):
        dp[1][j] = 2  # Only two choices for a single row
    
    # Fill dp table
    for i in range(2, N + 1):
        for j in range(2, M + 1):
            dp[i][j] = (dp[i-1][j] * dp[i][j-1]) % MOD
    
    return dp[N][M]

# Input handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    result = count_valid_matrices(N, M)
    print(result)

