MOD = 998244353

def count_valid_matrices(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base cases
    for i in range(N + 1):
        dp[i][0] = 1
    for j in range(M + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]) % MOD
    
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    result = count_valid_matrices(N, M)
    print(result)

