MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: there's one way to have an empty sequence
    dp[0][0] = 1
    
    # Iterate over positions in the sequence
    for i in range(1, N + 1):
        # Iterate over possible values to place at position i
        for j in range(1, N + 1):
            # Calculate the number of valid sequences ending with value j at position i
            for k in range(1, N + 1):
                if A[k-1] >= dp[i-1][k]:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Sum up all ways to form a sequence of length N
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))

# Get the result
result = count_valid_sequences(N, A)

# Print the result
print(result)

