MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the dp array with zeros
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: There's one way to form an empty sequence
    for j in range(N + 1):
        dp[0][j] = 1
    
    # Fill the dp array
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]  # Carry over the count from previous number j-1
            for k in range(1, min(A[j-1], i) + 1):
                dp[i][j] += dp[i-k][j-1]
                dp[i][j] %= MOD
    
    return dp[N][N]

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Get the result and print it
result = count_valid_sequences(N, A)
print(result)

