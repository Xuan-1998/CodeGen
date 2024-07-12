def count_valid_sequences(N, A):
    MOD = 998244353

    # Initialize the dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    # Fill the dp table
    for l in range(1, N + 1):
        for k in range(1, N + 1):
            if A[k - 1] >= l:
                dp[l][k] = sum(dp[l - 1][j] for j in range(1, N + 1) if A[j - 1] >= l) % MOD

    # Compute the final answer
    answer = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return answer

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Get the result
result = count_valid_sequences(N, A)

# Print the result
print(result)

