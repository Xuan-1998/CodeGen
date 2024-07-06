python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 2
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    
    # The answer is the number of valid N x M matrices
    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

# Get the result and print it
result = count_valid_matrices(N, M)
print(result)

