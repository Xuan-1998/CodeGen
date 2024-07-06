MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if k != j:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= MOD
    
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

