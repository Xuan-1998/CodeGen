MOD = 1000000007

def solve(N, K):
    # Initialize the DP array
    DP = [[0] * K for _ in range(N + 1)]
    DP[0][0] = 1  # Base case: Messi starts with the ball
    
    # Fill the DP array
    for i in range(1, N + 1):
        for j in range(K):
            # Calculate the number of ways for each player to receive the ball
            for k in range(K):
                if k != j:  # A player cannot pass the ball to themselves
                    DP[i][j] = (DP[i][j] + DP[i-1][k]) % MOD
                    
    # The answer is the number of ways Messi receives the ball after N passes
    return DP[N][0]

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(solve(N, K))
