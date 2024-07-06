python
MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize a dp table with dimensions (N+1) x (M+1)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: there's exactly one way to fill a 0x0 matrix (the empty matrix)
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]  # Adding a new row of all 0s or all 1s
                dp[i][j] %= MOD
            if j > 0:
                dp[i][j] += dp[i][j - 1]  # Adding a new column of all 0s or all 1s
                dp[i][j] %= MOD
            if i > 0 and j > 0:
                dp[i][j] -= dp[i - 1][j - 1]  # Avoid double counting the intersection
                dp[i][j] %= MOD
    
    # The answer is the number of ways to fill an N x M matrix
    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

# Compute the result
result = count_valid_matrices(N, M)

# Print the result
print(result)

