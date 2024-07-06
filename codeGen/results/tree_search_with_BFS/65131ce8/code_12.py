python
MOD = 998244353

def binomial_coefficients(n, mod):
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % mod
    return C

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Precompute binomial coefficients
    C = binomial_coefficients(N, MOD)
    
    # Fill the dp table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(i):
                dp[i][j] = (dp[i][j] + dp[k][j-1] * C[i-1][k] % MOD) % MOD
                dp[i][j] = (dp[i][j] + dp[k][j] * C[i-1][k] % MOD) % MOD
    
    # Sum up the results
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    # Print the result
    print(result)


