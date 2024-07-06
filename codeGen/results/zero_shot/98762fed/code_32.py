def count_valid_matrices(N, M):
    MOD = 998244353
    # Number of ways to select rows to be all ones
    rows_all_ones = pow(2, N, MOD)
    # Number of ways to select columns to be all ones
    columns_all_ones = pow(2, M, MOD)
    # Total valid matrices
    total_valid_matrices = (rows_all_ones * columns_all_ones) % MOD
    return total_valid_matrices

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

