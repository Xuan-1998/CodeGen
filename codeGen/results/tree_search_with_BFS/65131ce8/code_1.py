MOD = 998244353

def modinv(a, p):
    return pow(a, p-2, p)

def comb(n, k, fact, inv_fact):
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def preprocess_combinations(n, MOD):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[n] = modinv(fact[n], MOD)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

def solve(N, d):
    fact, inv_fact = preprocess_combinations(N, MOD)
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1
    
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                if d[k-1] > 0:
                    dp[i][j] += dp[k][j - 1] * comb(i - 1, k - 1, fact, inv_fact) % MOD
                    dp[i][j] %= MOD
    
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    print(solve(N, d))

