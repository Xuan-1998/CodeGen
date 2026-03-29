MOD = 998244353

def count_sequences(N, A):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: There's exactly one way to form an empty sequence
    for j in range(N + 1):
        dp[0][j] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]
            if i <= A[j-1]:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD

    return dp[N][N]

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

# Compute and print the result
result = count_sequences(N, A)
print(result)

