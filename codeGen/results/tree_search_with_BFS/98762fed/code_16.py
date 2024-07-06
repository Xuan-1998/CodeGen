python
import sys
input = sys.stdin.read

MOD = 998244353

def modinv(a, p):
    return pow(a, p - 2, p)

def binomial_coefficient(n, k, mod):
    if k > n:
        return 0
    num = den = 1
    for i in range(k):
        num = num * (n - i) % mod
        den = den * (i + 1) % mod
    return num * modinv(den, mod) % mod

def count_ones(N, M):
    # Calculate the binomial coefficient (N+M choose N) % MOD
    return binomial_coefficient(N + M, N, MOD)

def main():
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    result = count_ones(N, M)
    print(result)

if __name__ == "__main__":
    main()

