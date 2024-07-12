python
def count_sequences(N, A):
    MOD = 998244353
    
    # Initialize the dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: There is one way to form an empty sequence
    for j in range(N + 1):
        dp[0][j] = 1
    
    # Fill the dp array
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]
            if A[j-1] >= i:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
    
    # The answer is the number of ways to form a sequence of length N using the first N numbers
    return dp[N][N]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Compute the result
result = count_sequences(N, A)

# Print the result
print(result)

