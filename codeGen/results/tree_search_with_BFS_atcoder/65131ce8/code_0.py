MOD = 998244353

def solve():
    N = int(input().strip())
    d = list(map(int, input().strip().split()))
    if sum(d) != N - 1 or d[0] != 1:
        return 0
    dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    dp[1][1][0] = 1
    for i in range(2, N+1):
        for j in range(1, i+1):
            for k in range(1, min(i, d[i-1])+1):
                for l in range(k):
                    dp[i][j][k] = (dp[i][j][k] + dp[i-k][j-1][l] * dp[k][j][k-1]) % MOD
    return sum(dp[N][j][d[N-1]] * j for j in range(1, N+1)) % MOD

print(solve())

