MOD = 1000000007

def count_ways(N, K):
    # Initialize the dp array
    dp = [[0 for _ in range(K)] for _ in range(N+1)]
    dp[0][0] = 1
    
    # Fill in the dp array
    for i in range(1, N+1):
        for j in range(K):
            # If the ball is currently with Messi
            if j == 0:
                dp[i][j] = dp[i-1][1] * (K-1) % MOD
            else:
                # If the ball is passed back to Messi
                dp[i][j] = dp[i-1][0]
                # If the ball is passed to another player
                if j > 1:
                    dp[i][j] += dp[i-1][j-1] * (j-1)
                dp[i][j] %= MOD
    
    return dp[N][0]

# Read number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(count_ways(N, K))
