python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize the dp table with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: 1x1 matrix
    dp[1][1] = 2
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            if i > 1:
                dp[i][j] += dp[i - 1][j]
            if j > 1:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD
    
    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

# Print the result
print(count_valid_matrices(N, M))

