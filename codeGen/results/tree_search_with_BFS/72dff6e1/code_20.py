python
MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    # Initialize count array to keep track of occurrences
    count = [0] * (N + 1)

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if count[j] < A[j - 1]:
                for k in range(1, N + 1):
                    if k != j:
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
                count[j] += 1

    # Sum up the results for sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Calculate the result
result = count_valid_sequences(N, A)

# Print the result
print(result)

