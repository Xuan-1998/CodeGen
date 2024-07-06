MOD = 998244353

def count_valid_matrices(N, M):
    # The base case: If N or M is 1, any matrix is valid
    if N == 1 or M == 1:
        return pow(2, N * M, MOD)
    
    # Initialize a table to store the number of valid matrices for each subproblem
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: A 1x1 matrix can be either 0 or 1
    dp[1][1] = 2
    
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if n == 1 and m == 1:
                continue
            dp[n][m] = (dp[n - 1][m] * dp[1][m] + dp[n][m - 1] * dp[n][1] - dp[n - 1][m - 1] * dp[1][1]) % MOD
    
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

