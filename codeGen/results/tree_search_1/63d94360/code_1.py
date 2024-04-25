MOD = 1000000007

def ways_to_pass_ball(N, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][1] = 1  # Messi starts with the ball
    
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if j == 1:
                dp[i][j] = sum(dp[i-1][k] for k in range(2, K + 1)) % MOD
            else:
                dp[i][j] = (dp[i-1][1] * (K - 1) + dp[i-1][j] * (K - 2)) % MOD
    
    return dp[N][1]

# Read input from stdin and print output to stdout
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(ways_to_pass_ball(N, K))
