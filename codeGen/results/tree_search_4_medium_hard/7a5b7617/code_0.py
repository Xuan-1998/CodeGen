def solve():
    T = int(input())
    MOD = 10**9 + 7
    
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for s in range(M+1):
            if i == 1:
                dp[i][s] = 1
            else:
                dp[i][s] = sum(dp[i-1][k] for k in range(s+1)) % MOD
    
    print(sum(dp[N][m] for m in range(M+1)) % MOD)

solve()
