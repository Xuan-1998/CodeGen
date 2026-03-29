def count_valid_matrices(N, M):
    MOD = 998244353
    result = (N * M) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

