def count_valid_matrices(N, M):
    MOD = 998244353

    # dp[r][c] will store the number of valid matrices of size r x c
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to have an empty matrix

    # Fill the dp table
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            dp[r][c] = (dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1]) % MOD

    # The answer is the number of ways to fill an N x M matrix
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    result = count_valid_matrices(N, M)
    print(result)

