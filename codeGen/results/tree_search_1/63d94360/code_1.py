MOD = 1000000007

def solve(N, K):
    # Initialize the dp array
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[1][1] = K-1  # Messi can receive the ball from any of the other K-1 players
    
    # Fill the dp array
    for i in range(2, N+1):
        for j in range(1, min(i, K)+1):
            if j == 1:
                # If Messi is to receive the ball for the first time
                dp[i][j] = dp[i-1][j] * (K-1) % MOD
            else:
                # Messi has already received the ball before
                dp[i][j] = (dp[i-1][j] * (K-2) + dp[i-1][j-1] * (K-1)) % MOD
    
    # The answer is the number of ways to pass the ball N times with Messi receiving it exactly once on the final pass
    return dp[N][1]

# Read the number of test cases
T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(solve(N, K))
