python
def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize the DP array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]
            for k in range(1, min(A[j-1], i) + 1):
                dp[i][j] = (dp[i][j] + dp[i-k][j-1]) % MOD
    
    # The answer is the number of valid sequences of length N using the first N numbers
    return dp[N][N]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Compute the result
result = count_valid_sequences(N, A)

# Print the result
print(result)

