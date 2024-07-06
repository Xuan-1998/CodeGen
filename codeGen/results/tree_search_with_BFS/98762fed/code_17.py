python
def count_matrices(N, M):
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: 0x0 matrix
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Number of valid matrices of size i x j is 2^(i*j) modulo MOD
            dp[i][j] = pow(2, i * j, MOD)
    
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    result = count_matrices(N, M)
    print(result)

