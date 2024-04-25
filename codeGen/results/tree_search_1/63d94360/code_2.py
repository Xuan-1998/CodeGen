MOD = 1000000007

def solve(N, K):
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(i+1):
            if j > 0:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] * (K-1)) % MOD
            else:
                dp[i][j] = (dp[i-1][j] * (K-1)) % MOD
    
    return dp[N][1]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))
