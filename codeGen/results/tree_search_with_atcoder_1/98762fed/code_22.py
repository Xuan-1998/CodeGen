def mod_binomial(n, k, mod):
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    denom = 1
    for i in range(k):
        num = num * (n - i) % mod
        denom = denom * (i + 1) % mod
    return num * pow(denom, mod - 2, mod) % mod

def count_valid_matrices(N, M, mod=998244353):
    # Total number of valid matrices is 2^(N+M-1)
    total = pow(2, (N + M - 1), mod)
    return total

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

