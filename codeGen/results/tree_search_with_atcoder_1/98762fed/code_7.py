import sys
input = sys.stdin.read

MOD = 998244353

def binomial_coefficient(n, k, mod):
    if n < k:
        return 0
    if k == 0 or n == k:
        return 1
    num = 1
    den = 1
    for i in range(k):
        num = num * (n - i) % mod
        den = den * (i + 1) % mod
    return num * pow(den, mod - 2, mod) % mod

def count_valid_matrices(N, M):
    return binomial_coefficient(N + M - 2, N - 1, MOD)

def main():
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

if __name__ == "__main__":
    main()

