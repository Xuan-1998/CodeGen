python
def count_valid_matrices(N, M):
    MOD = 998244353
    total_matrices = pow(2, N + M, MOD)
    return total_matrices

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

