MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1
    
    # Precompute factorials and inverse factorials for combinatorial calculations
    fact = [1] * (N + 1)
    inv_fact = [1] * (N + 1)
    
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    def comb(n, k):
        if n < k or k < 0:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    
    # Fill the dp table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                dp[i][j] = (dp[i][j] + dp[k][j - 1] * comb(i - 1, k - 1) % MOD) % MOD
    
    # Calculate the result
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)


