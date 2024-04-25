MOD = 1000000007

def ways_to_pass(N, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][1] = 1

    for i in range(1, N + 1):
        for j in range(2, K + 1):
            # Pass to Messi (j-1 choices)
            dp[i][j] = (dp[i-1][j] * (j-1)) % MOD
            # Pass to another player (1 choice if Messi had the ball, j-1 choices if not)
            dp[i][j] = (dp[i][j] + dp[i-1][j-1] * (j-1)) % MOD

    return dp[N][K]

def main():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().split())
        print(ways_to_pass(N, K))

if __name__ == "__main__":
    main()
