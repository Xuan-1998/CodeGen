MOD = 1000000007

def count_ways(N, K):
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][1] = 1
    
    for i in range(1, N+1):
        for j in range(1, K+1):
            if j == 1:
                dp[i][j] = dp[i-1][j+1] % MOD
            elif j == K:
                dp[i][j] = dp[i-1][j-1] % MOD
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD
    
    return dp[N][1]

# Read the number of test cases
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(count_ways(N, K))
