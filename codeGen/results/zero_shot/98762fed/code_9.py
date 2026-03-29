def count_valid_matrices(N, M):
    MOD = 998244353

    # dp[i][j] will store the number of ways to fill an i x j matrix
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: There's one way to fill a 0x0 matrix (with no elements)
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            if i > 0 and j > 0:
                dp[i][j] -= dp[i - 1][j - 1]
            
            dp[i][j] %= MOD
    
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    print(count_valid_matrices(N, M))

