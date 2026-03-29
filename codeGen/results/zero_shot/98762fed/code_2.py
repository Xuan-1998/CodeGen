def count_valid_matrices(N, M):
    MOD = 998244353
    
    # dp[i][j] will be the number of valid matrices of size i x j
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: There's exactly one way to form a 0 x 0 matrix
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Sum of all dp[i-1][k] for k <= j
            dp[i][j] = sum(dp[i-1][:j+1]) % MOD
    
    # The answer is the number of valid matrices of size N x M
    result = dp[N][M]
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

