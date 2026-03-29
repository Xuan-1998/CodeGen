MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize the dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Each element can be either 0 or 1, thus there are 2 choices for each element
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + MOD) % MOD

    # The answer is dp[N][M]
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

