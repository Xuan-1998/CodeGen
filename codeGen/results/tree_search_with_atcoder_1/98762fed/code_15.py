python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize DP table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base cases
    for i in range(N + 1):
        dp[i][0] = 1
    for j in range(M + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    
    # The result is the number of valid matrices of size N x M
    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

# Print the result
print(count_valid_matrices(N, M))

