def solve():
    T = int(input())
    MOD = 10**9 + 7
    
    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M+1) for _ in range(N+1)]
        
        # Base case: dp[0][j] = 1 for all j
        for j in range(M+1):
            dp[0][j] = 1
        
        for i in range(1, N+1):
            for j in range(1, M+1):
                dp[i][j] = (dp[i-1][0:j] * (M - sum(dp[i-1][:j]))) % MOD
        print(dp[N-1][M-1])

solve()
