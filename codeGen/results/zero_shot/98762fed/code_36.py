python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize the dp table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case
    dp[0][0] = 1
    
    # Fill the dp table
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
                dp[i][j] = (dp[i][j] + MOD) % MOD
    
    # The answer is the number of valid matrices of size N x M
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

