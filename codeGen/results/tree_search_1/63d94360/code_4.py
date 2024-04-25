MOD = 1000000007

def solve(N, K):
    # Initialize the DP table with zeros
    dp = [[0] * (K+1) for _ in range(N+1)]
    # Base case: Messi has the ball at the start without any passes
    dp[0][0] = 1

    # Fill the DP table
    for i in range(1, N+1):
        for j in range(K+1):
            if j == 0:
                # If Messi is to receive the ball, it can come from any other player
                for k in range(1, K+1):
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
            else:
                # If some other player is to receive the ball, it can come from any player including Messi
                for k in range(K+1):
                    if k != j:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

    # The answer is the number of ways Messi can receive the ball after exactly N passes
    return dp[N][0]

# Read the number of test cases
T = int(input().strip())
for _ in range(T):
    # Read N and K for each test case
    N, K = map(int, input().strip().split())
    print(solve(N, K))
