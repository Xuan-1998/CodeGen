def count_ones(N, M):
    MOD = 998244353
    total_elements = N * M
    total_matrices = pow(2, total_elements, MOD)
    total_ones = (total_elements * total_matrices // 2) % MOD
    return total_ones

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    result = count_ones(N, M)
    print(result)

