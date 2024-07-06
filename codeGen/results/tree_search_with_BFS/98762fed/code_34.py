MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize a 2D dp array with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: 1x1 matrix can be either 0 or 1, so there are 2 valid matrices
    dp[1][1] = 2
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            # If we add a new row to an (i-1)xj matrix
            if i > 1:
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
            # If we add a new column to an ix(j-1) matrix
            if j > 1:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
            # Avoid double counting the base case for (1,1)
            if i > 1 and j > 1:
                dp[i][j] = (dp[i][j] - dp[i-1][j-1] + MOD) % MOD
    
    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

# Compute the result
result = count_valid_matrices(N, M)

# Output the result
print(result)

