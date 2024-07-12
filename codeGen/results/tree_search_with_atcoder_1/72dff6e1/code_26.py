python
MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    for j in range(N + 1):
        dp[0][j] = 1
    
    # Fill dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]
            if i <= A[j-1]:
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
    
    return dp[N][N]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Calculate the result
result = count_valid_sequences(N, A)

# Print the result
print(result)

