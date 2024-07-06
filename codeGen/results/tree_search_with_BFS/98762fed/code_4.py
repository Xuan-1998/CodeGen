MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize the dp table with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: 0x0 matrix is trivially valid

    # Iterate through all possible matrix sizes
    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD
            if i > 0 and j > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

    # The answer is the number of valid matrices of size N x M
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

