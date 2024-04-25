MOD = 1000000007

def count_ways(N, K):
    # Initialize the dp table with zeros
    dp = [[0 for _ in range(K)] for _ in range(N+1)]
    dp[0][0] = 1  # Base case

    # Fill the dp table
    for i in range(1, N+1):  # Number of passes
        for j in range(K):  # Current player with the ball
            if j == 0:  # If Messi has the ball
                for k in range(1, K):  # He can pass to any other player
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
            else:  # If another player has the ball
                # They can pass it to Messi
                dp[i][j] = (dp[i][j] + dp[i-1][0]) % MOD
                # Or to any other player except themselves and Messi
                for k in range(1, K):
                    if k != j:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

    # The answer is the number of ways to pass the ball N times ending with Messi
    return dp[N][0]

# Read the number of test cases from stdin
T = int(input().strip())
for _ in range(T):
    # Read N and K for each test case
    N, K = map(int, input().strip().split())
    # Output the answer for each test case
    print(count_ways(N, K))
