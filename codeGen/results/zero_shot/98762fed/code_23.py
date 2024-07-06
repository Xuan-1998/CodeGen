def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: there's one way to have a 0x0 matrix (the empty matrix)
    dp[0][0] = 1
    
    # Fill the dp array
    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
            if i > 0 and j > 0:
                dp[i][j] = (dp[i][j] - dp[i-1][j-1] + MOD) % MOD
    
    # The answer is the number of valid NxM matrices
    return dp[N][M]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

# Compute and print the result
print(count_valid_matrices(N, M))

