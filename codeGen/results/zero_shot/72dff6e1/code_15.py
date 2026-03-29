def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[j - 1] >= i:
                for k in range(N + 1):
                    if k + 1 <= A[j - 1]:
                        dp[j][k + 1] = (dp[j][k + 1] + dp[j - 1][k]) % MOD
                    dp[j][k] = (dp[j][k] + dp[j - 1][k]) % MOD
    
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[j][A[j - 1]]) % MOD
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Compute and print the result
print(count_valid_sequences(N, A))

