MOD = 998244353

def count_valid_matrices(N, M):
    # dp[i][j] will store the number of valid matrices of size i x j
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: 1x1 matrix can be either [0] or [1]
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

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

# Calculating the number of valid matrices
result = count_valid_matrices(N, M)
print(result)

