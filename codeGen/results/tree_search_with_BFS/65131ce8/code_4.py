MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(0, i):
            for k in range(0, i - j):
                if j + k <= N and k <= d[i - 1]:
                    dp[i][j + 1] += dp[i - 1 - k][j] * comb(i - 1, k)
                    dp[i][j + 1] %= MOD
    
    result = 0
    for j in range(1, N + 1):
        result += dp[N][j]
        result %= MOD
    
    print(result)

def comb(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    denom = 1
    for i in range(k):
        num = num * (n - i) % MOD
        denom = denom * (i + 1) % MOD
    return num * pow(denom, MOD - 2, MOD) % MOD

if __name__ == "__main__":
    solve()

