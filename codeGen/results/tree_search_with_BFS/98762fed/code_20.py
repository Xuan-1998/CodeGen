python
MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize dp table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base cases
    for i in range(1, N + 1):
        dp[i][1] = pow(2, i, MOD)
    for j in range(1, M + 1):
        dp[1][j] = pow(2, j, MOD)
    
    # Fill dp table
    for i in range(2, N + 1):
        for j in range(2, M + 1):
            dp[i][j] = pow(2, i * j, MOD)  # All possible matrices of size i x j
    
    # Result is the number of valid matrices of size N x M
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    result = count_valid_matrices(N, M)
    print(result)

