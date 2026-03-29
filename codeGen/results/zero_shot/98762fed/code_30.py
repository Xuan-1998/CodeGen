def count_valid_matrices(N, M):
    MOD = 998244353

    # Calculate the number of valid matrices
    valid_matrices = pow(2, N, MOD) * pow(2, M, MOD) % MOD

    return valid_matrices

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

