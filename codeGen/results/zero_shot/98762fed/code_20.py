def count_matrices(N, M):
    MOD = 998244353
    
    # Initialize the dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: one way to fill a 0x0 matrix
    dp[0][0] = 1
    
    # Fill the dp array
    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
                dp[i][j] %= MOD
            if j > 0:
                dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD
            if i > 0 and j > 0:
                dp[i][j] -= dp[i - 1][j - 1]
                dp[i][j] += MOD
                dp[i][j] %= MOD
    
    # The result is the number of ways to fill the NxM matrix
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_matrices(N, M))

