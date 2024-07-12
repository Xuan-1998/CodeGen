python
MOD = 998244353

def comb(n, k, fact, inv_fact):
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def precompute_factorials(max_n):
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

def solve(N, M):
    max_n = N + M
    fact, inv_fact = precompute_factorials(max_n)
    
    # We need to count the number of non-decreasing sequences of length M with elements from 0 to N
    # This is equivalent to choosing M positions out of (M + N - 1) positions
    result = comb(M + N - 1, N - 1, fact, inv_fact) ** N % MOD
    
    print(result)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    solve(N, M)

