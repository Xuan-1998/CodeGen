python
def count_valid_matrices(N, M):
    MOD = 998244353

    # Initialize the dp array
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: 1 way to have an empty matrix

    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Calculate the number of valid matrices for size i x j
            dp[i][j] = (dp[i - 1][j] * dp[1][j] + dp[i][j - 1] * dp[i][1] - dp[i - 1][j - 1] * dp[1][1]) % MOD

    # The answer is the number of valid N x M matrices
    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

# Get the result
result = count_valid_matrices(N, M)

# Print the result
print(result)

