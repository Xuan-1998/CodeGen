MOD = 998244353

def power_mod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_valid_matrices(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case initialization
    for i in range(1, N + 1):
        dp[i][1] = power_mod(2, i, MOD)
    for j in range(1, M + 1):
        dp[1][j] = power_mod(2, j, MOD)
    
    # Fill DP table
    for i in range(2, N + 1):
        for j in range(2, M + 1):
            dp[i][j] = power_mod(2, i * j, MOD)
            for a in range(1, i):
                for b in range(1, j):
                    if (a < i and b < j):
                        dp[i][j] -= dp[a][b]
                        dp[i][j] %= MOD
    
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

