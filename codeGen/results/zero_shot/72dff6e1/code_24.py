python
def count_sequences(N, A):
    MOD = 998244353
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: One way to form an empty sequence
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(N + 1):
            # Carry forward the previous counts
            dp[i][j] = dp[i-1][j]
            if j > 0:
                # Add ways to include one more i
                dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    
    # Result is the sum of all ways to form sequences of length N
    result = 0
    for j in range(N + 1):
        if j <= A[j-1]:
            result += dp[N][j]
            result %= MOD
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Get the result and print it
result = count_sequences(N, A)
print(result)

