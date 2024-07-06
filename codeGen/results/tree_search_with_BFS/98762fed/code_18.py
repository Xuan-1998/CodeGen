MOD = 998244353

def count_valid_matrices(N, M):
    # Function to compute binomial coefficients modulo MOD
    def binomial_coeff(n, k, mod):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        num = den = 1
        for i in range(k):
            num = num * (n - i) % mod
            den = den * (i + 1) % mod
        return num * pow(den, mod - 2, mod) % mod
    
    # Total number of ways to place N*M elements in a matrix is 2^(N*M)
    total_ways = pow(2, N * M, MOD)
    
    # Calculate the number of valid matrices
    valid_matrices = 0
    for i in range(N + 1):
        for j in range(M + 1):
            # Calculate the number of ways to place i 1s in N rows and j 1s in M columns
            ways_rows = binomial_coeff(N, i, MOD)
            ways_cols = binomial_coeff(M, j, MOD)
            valid_matrices = (valid_matrices + ways_rows * ways_cols) % MOD
    
    return valid_matrices

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

# Calculate and print the result
result = count_valid_matrices(N, M)
print(result)

