python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Function to compute factorial % MOD
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result = (result * i) % MOD
        return result
    
    # Function to compute nCr % MOD using Fermat's Little Theorem for modular inverse
    def nCr(n, r):
        if r > n:
            return 0
        num = factorial(n)
        denom = (factorial(r) * factorial(n - r)) % MOD
        return (num * pow(denom, MOD - 2, MOD)) % MOD
    
    # Calculate the number of valid matrices
    total_ones = 0
    for i in range(N + 1):
        for j in range(M + 1):
            # Number of ways to distribute i 1's in N rows and j 1's in M columns
            total_ones = (total_ones + nCr(N, i) * nCr(M, j)) % MOD
    
    return total_ones

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

