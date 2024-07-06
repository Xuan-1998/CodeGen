python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # All elements can be 0 or 1, total 2^(N*M) matrices
    total_matrices = pow(2, N * M, MOD)
    
    # Return the result modulo 998244353
    return total_matrices

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    result = count_valid_matrices(N, M)
    print(result)

