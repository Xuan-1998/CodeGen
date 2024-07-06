python
MOD = 998244353

def modinv(a, p):
    return pow(a, p - 2, p)

def precompute_binomial_coefficients(n, mod):
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod
    return C

def solve(N, d):
    C = precompute_binomial_coefficients(N, MOD)
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1
    
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(i):
                if j > 1:
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * C[i - 1][k]) % MOD
                dp[i][j] = (dp[i][j] + dp[k][j] * C[i - 1][k]) % MOD
    
    result = 0
    for i in range(1, N + 1):
        result = (result + dp[N][i] * i) % MOD
    
    print(result)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    solve(N, d)

