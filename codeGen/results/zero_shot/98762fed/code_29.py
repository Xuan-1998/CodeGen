MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize a 2D DP array with all zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: there's one way to fill a 0x0 matrix
    dp[0][0] = 1
    
    # Fill the DP table
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
                dp[i][j] %= MOD
    
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

