python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Validate input constraints
    assert 2 <= N <= 500
    assert len(d) == N
    assert sum(d) == N - 1
    assert d[0] >= 1
    for di in d:
        assert 0 <= di <= N - 1
    
    # Function to calculate factorials and modular inverses
    def factorials_and_inverses(n, mod):
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % mod
        inv_fact[n] = pow(fact[n], mod - 2, mod)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
        return fact, inv_fact
    
    # Calculate factorials and inverses up to N
    fact, inv_fact = factorials_and_inverses(N, MOD)
    
    # Function to calculate binomial coefficient
    def binom(n, k, mod):
        if n < k or k < 0:
            return 0
        return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod
    
    # Dynamic programming table to store the number of ways to form trees
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(N + 1):
            for k in range(1, N + 1):
                if j >= k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k] * binom(j, k, MOD)) % MOD
    
    # Calculate the number of good vertices
    good_vertices = 0
    for i in range(1, N + 1):
        good_vertices = (good_vertices + dp[N][i]) % MOD
    
    print(good_vertices)


