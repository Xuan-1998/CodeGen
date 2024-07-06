python
MOD = 998244353

def count_valid_matrices(N, M):
    # Create a dp table with dimensions (N+1) x (M+1)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: A 1x1 matrix can be either 0 or 1
    dp[1][1] = 2
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            # Calculate dp[i][j] based on smaller subproblems
            dp[i][j] = (dp[i-1][j] * dp[1][j] + dp[i][j-1] * dp[i][1] - dp[i-1][j-1] * dp[1][1]) % MOD
    
    # The answer is the number of valid matrices of size N x M
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

