python
MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the DP table with zeros
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: there is exactly one way to form an empty sequence
    for j in range(N + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]  # Exclude the j-th number
            if i - 1 >= 0:
                dp[i][j] += dp[i-1][j-1] * min(A[j-1], i)
                dp[i][j] %= MOD  # Take modulo at each step to avoid overflow
    
    # The result is the number of valid sequences of length N using numbers from 1 to N
    return dp[N][N]

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

# Calculate and print the result
print(count_valid_sequences(N, A))

