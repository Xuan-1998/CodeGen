MOD = 998244353

def count_valid_sequences(N, A):
    # dp[i][j] will be the number of valid sequences of length i where the last number is j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: single element sequences
    for j in range(1, N + 1):
        dp[1][j] = 1 if A[j-1] >= 1 else 0
    
    # Fill the dp table
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if A[k-1] >= i - 1 and A[j-1] >= 1:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Sum up all valid sequences of length N
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Print the result
print(count_valid_sequences(N, A))

