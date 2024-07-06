python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initializing the dp table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: One way to fill a 1x1 matrix
    dp[1][1] = 2  # Either 0 or 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + MOD) % MOD
    
    # The final answer is the number of ways to fill an NxM matrix
    return dp[N][M]

# Reading input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

# Printing the result
print(count_valid_matrices(N, M))

