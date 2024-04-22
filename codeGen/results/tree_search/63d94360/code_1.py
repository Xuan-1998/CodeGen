MOD = 1000000007

# Function to calculate the number of ways to pass the ball
def count_passes(N, K):
    # Initialize the DP array with zeros
    DP = [[0 for _ in range(K)] for _ in range(N+1)]
    DP[0][0] = 1  # Base case

    # Calculate the number of ways for each number of passes
    for i in range(1, N+1):
        for j in range(K):
            # Sum the ways from all other players in the previous pass
            for k in range(K):
                if k != j:  # Player cannot pass to themselves
                    DP[i][j] = (DP[i][j] + DP[i-1][k]) % MOD

    # Return the number of ways Messi (player 0) can receive the ball after N passes
    return DP[N][0]

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(count_passes(N, K))
