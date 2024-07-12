python
MOD = 998244353

def count_valid_matrices(N, M):
    # dp[i][j] will be the number of ways to fill a i x j matrix
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: There's exactly one way to fill a 0 x j or i x 0 matrix (the empty matrix)
    for i in range(N + 1):
        dp[i][0] = 1
    for j in range(M + 1):
        dp[0][j] = 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD
    
    # The answer is the number of ways to fill an N x M matrix
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

