def count_valid_sequences(N, A):
    MOD = 998244353

    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]
            for k in range(1, A[j-1] + 1):
                if i - k >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-k][j-1]) % MOD
    
    return dp[N][N]

# Reading input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Calculating and printing the result
print(count_valid_sequences(N, A))

