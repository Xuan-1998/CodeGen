MOD = 1000000007

def ways_to_pass(N, K):
    dp = [[0] * K for _ in range(N + 1)]
    dp[0][0] = 1  # Base case

    for i in range(1, N + 1):
        for j in range(K):
            for k in range(K):
                if k != j:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= MOD

    return dp[N][0]

# Read number of test cases
T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(ways_to_pass(N, K))
