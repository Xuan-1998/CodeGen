python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize the dp table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: 1x1 matrix
    dp[1][1] = 2  # [0] and [1]
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            # Calculate dp[i][j] based on smaller matrices
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD
    
    # The result is the number of valid NxM matrices
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

