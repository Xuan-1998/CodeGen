MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the DP table
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1  # Base case: one way to form an empty sequence
    
    # Fill the DP table
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i][j-1]  # Not using the j-th number
            if i - 1 <= A[j-1]:  # Check if we can use the j-th number
                dp[i][j] = (dp[i][j] + dp[i-1][j] * (A[j-1] - (i-1))) % MOD
    
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

