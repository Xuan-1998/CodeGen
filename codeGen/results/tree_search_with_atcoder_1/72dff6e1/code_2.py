MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Iterate over the length of the sequence
    for i in range(1, N + 1):
        # Iterate over all possible last elements
        for j in range(1, N + 1):
            # Iterate over all possible previous elements
            for k in range(1, N + 1):
                # Check the validity of adding element j to the sequence ending with k
                if dp[i-1][k] > 0 and A[j-1] > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
                    A[j-1] -= 1
    
    # Compute the final answer
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

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

