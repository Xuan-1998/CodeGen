python
MOD = 998244353

def count_valid_matrices(N, M):
    # Precompute powers of 2 up to N*M
    pow2 = [1] * (N * M + 1)
    for i in range(1, N * M + 1):
        pow2[i] = (pow2[i - 1] * 2) % MOD

    # Initialize result
    result = 0

    # Iterate over all possible counts of 1s in the matrix
    for ones in range(N + 1):
        for cols in range(M + 1):
            # Calculate the number of ways to choose 'ones' rows and 'cols' columns
            ways = (pow2[ones * cols] - 1) % MOD
            result = (result + ways) % MOD

    return result

# Input reading
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

# Calculate and print the result
print(count_valid_matrices(N, M))

