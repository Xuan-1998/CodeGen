MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize dp array with zeros
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: single element sequences
    for j in range(1, N + 1):
        dp[1][j] = 1
    
    # Iterate over sequence lengths from 2 to N
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                # Check constraints
                if dp[i-1][k] > 0 and A[j-1] >= i - 1 and A[k-1] >= i - 1:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Output the result
print(count_valid_sequences(N, A))

