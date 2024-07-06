def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: There's exactly one way to form an empty sequence
    for j in range(N + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]
            if A[j-1] >= i:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
    
    # The answer is the number of valid sequences of length N using the first N elements
    return dp[N][N]

# Reading input from stdin
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Calculate and print the result
print(count_valid_sequences(N, A))

