import sys

def count_steady_tables(N, M):
    MOD = 10**9 + 7
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    for i in range(2, N + 1):
        for j in range(M + 1):
            if j <= M:
                dp[i][j] = sum(dp[k][j] for k in range(i)) % MOD
    
    total = 0
    for i in range(N + 1):
        for j in range(M + 1):
            total += dp[i][j]
            total %= MOD
    
    return total

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(count_steady_tables(N, M))
