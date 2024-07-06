MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if i <= A[k - 1]:
                    dp[i][k] = (dp[i][k] + dp[i - 1][j]) % MOD
    
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

# Output result
print(count_valid_sequences(N, A))

