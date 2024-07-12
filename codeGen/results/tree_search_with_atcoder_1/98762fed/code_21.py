MOD = 998244353

def count_valid_matrices(N, M):
    # We can use combinatorial properties to count the valid matrices
    # Total number of matrices is 2^(N*M)
    total_matrices = pow(2, N * M, MOD)
    return total_matrices

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    result = count_valid_matrices(N, M)
    print(result)

