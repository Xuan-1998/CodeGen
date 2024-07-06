python
def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize the dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: there is exactly one valid sequence of length 0 (the empty sequence)
    for j in range(1, N + 1):
        dp[0][j] = 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i-1][k] > 0 and dp[i-1][j] < A[j]:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Calculate the result
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Print the result
print(count_valid_sequences(N, A))

