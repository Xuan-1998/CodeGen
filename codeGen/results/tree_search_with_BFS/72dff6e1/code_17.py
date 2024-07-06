MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: dp[0][j] = 1 for all j (empty sequence)
    for j in range(1, N + 1):
        dp[0][j] = 1
    
    # Iterate through lengths from 1 to N
    for i in range(1, N + 1):
        # Cumulative sum array to efficiently compute the sum of dp[i-1][k]
        cumulative_sum = [0] * (N + 1)
        for k in range(1, N + 1):
            cumulative_sum[k] = (cumulative_sum[k - 1] + dp[i - 1][k]) % MOD
        
        for j in range(1, N + 1):
            # Number of valid sequences ending with j
            dp[i][j] = (cumulative_sum[j] - cumulative_sum[max(0, j - A[j - 1] - 1)]) % MOD
    
    # Calculate the final result
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Get the result and print it
result = count_valid_sequences(N, A)
print(result)

