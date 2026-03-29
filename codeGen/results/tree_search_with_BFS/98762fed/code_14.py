def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize a 2D DP array with all elements set to 0
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: There's one way to form a 0x0 matrix (trivially valid)
    dp[0][0] = 1
    
    # Fill the DP table
    for n in range(N + 1):
        for m in range(M + 1):
            if n > 0:
                dp[n][m] += dp[n - 1][m]
                dp[n][m] %= MOD
            if m > 0:
                dp[n][m] += dp[n][m - 1]
                dp[n][m] %= MOD
            if n > 0 and m > 0:
                dp[n][m] -= dp[n - 1][m - 1]
                dp[n][m] %= MOD
    
    # The answer is the number of valid matrices of size N x M
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

