python
def count_ones(N, M):
    MOD = 998244353
    # Total number of matrices is 2^(N*M)
    total_matrices = pow(2, N * M, MOD)
    # Each matrix has N*M elements, half of them on average are 1s
    # So, the expected number of 1s in one matrix is N*M / 2
    # We need to multiply this by the total number of matrices
    total_ones = (total_matrices * (N * M) // 2) % MOD
    return total_ones

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_ones(N, M))

