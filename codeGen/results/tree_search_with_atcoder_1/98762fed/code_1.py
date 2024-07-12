python
MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 2
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD
    
    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

# Calculate the result
result = count_valid_matrices(N, M)

# Print the result
print(result)

