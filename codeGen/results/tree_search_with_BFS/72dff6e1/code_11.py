python
def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize the dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Frequency array to keep track of occurrences
    freq = [0] * (N + 1)
    
    # Update dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if freq[j] < A[j - 1]:
                for k in range(1, N + 1):
                    if j != k and freq[k] < A[k - 1]:
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
                freq[j] += 1
    
    # Calculate the final answer
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

