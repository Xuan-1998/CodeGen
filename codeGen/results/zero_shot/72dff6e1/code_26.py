def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to form sequence of length 0
    
    # Iterate over each number from 1 to N
    for i in range(1, N + 1):
        # Iterate over each length from 0 to N
        for j in range(N + 1):
            # Carry over the previous counts
            dp[i][j] = dp[i - 1][j]
            # Add counts for using the current number up to A[i-1] times
            for k in range(1, min(A[i - 1], j) + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
    
    # The answer is the number of ways to form a sequence of length N using all numbers 1 to N
    return dp[N][N]

# Input reading
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Compute and print the answer
print(count_valid_sequences(N, A))

