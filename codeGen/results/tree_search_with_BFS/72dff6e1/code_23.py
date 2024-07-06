MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: empty sequence

    # Iterate over the length of the sequence
    for i in range(1, N + 1):
        # Iterate over the possible last elements of the sequence
        for j in range(1, N + 1):
            # Sum up all valid sequences of length i-1
            for k in range(1, N + 1):
                if j != k and dp[i-1][k] > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

    # Calculate the final answer
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

