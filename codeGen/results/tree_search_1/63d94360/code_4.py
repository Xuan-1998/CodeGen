MOD = 1000000007

def solve(N, K):
    dp = [[0 for _ in range(K)] for _ in range(N+1)]
    dp[0][0] = 1  # Messi starts with the ball

    for i in range(1, N+1):
        for j in range(K):
            for k in range(K):
                if k != j:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= MOD

    return dp[N][0]

T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(solve(N, K))
