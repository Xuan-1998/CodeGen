python
def count_valid_matrices(N, M):
    MOD = 998244353

    # dp[r][c] will store the number of valid matrices of size r x c
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Base case: 1x1 matrix has 2 possibilities (either 0 or 1)
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 or j == 1:
                dp[i][j] = 2 ** (i * j)
            else:
                dp[i][j] = (dp[i-1][j] * dp[i][j-1]) % MOD

    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

# Compute the result
result = count_valid_matrices(N, M)

# Output the result
print(result)

