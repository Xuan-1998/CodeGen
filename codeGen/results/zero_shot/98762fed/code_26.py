def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize a 2D dp array with 0
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: There's one way to have a 0x0 matrix (empty matrix)
    dp[0][0] = 1
    
    # Fill the dp table
    for n in range(N + 1):
        for m in range(M + 1):
            if n > 0:
                dp[n][m] = (dp[n][m] + dp[n-1][m]) % MOD
            if m > 0:
                dp[n][m] = (dp[n][m] + dp[n][m-1]) % MOD
            if n > 0 and m > 0:
                dp[n][m] = (dp[n][m] - dp[n-1][m-1] + MOD) % MOD
    
    # The number of valid matrices is stored in dp[N][M]
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    result = count_valid_matrices(N, M)
    print(result)

