MOD = 998244353

def binomial_coefficient(n, k, mod):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = den = 1
    for i in range(k):
        num = num * (n - i) % mod
        den = den * (i + 1) % mod
    return num * pow(den, mod - 2, mod) % mod

def count_valid_matrices(N, M):
    # For each possible number of 1s from 0 to N*M, calculate the number of valid matrices
    total_ones = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            total_ones += binomial_coefficient(N * M, i * j, MOD)
            total_ones %= MOD
    return total_ones

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

if __name__ == "__main__":
    main()

