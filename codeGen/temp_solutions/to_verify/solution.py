MOD = 1000000007

def solve(N, K):
    dp = [[0] * K for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        # Calculate the sum of ways to pass to Messi from any player
        sum_to_messi = sum(dp[i-1][1:]) % MOD
        # Messi has the ball
        dp[i][0] = sum_to_messi
        # Other players have the ball
        for j in range(1, K):
            dp[i][j] = (dp[i-1][0] + sum_to_messi - dp[i-1][j]) % MOD

    # The answer is the number of ways Messi can receive the ball after N passes
    return dp[N][0]

# Read the number of test cases
T = int(input().strip())
for _ in range(T):
    # Read N and K for each test case
    N, K = map(int, input().strip().split())
    print(solve(N, K))