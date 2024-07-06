MOD = 998244353

def binomial_coefficient(n, k, mod):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    inv_fact[n] = pow(fact[n], mod - 2, mod)
    
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    result = binomial_coefficient(N + M - 2, N - 1, MOD)
    print(result)

if __name__ == "__main__":
    main()

