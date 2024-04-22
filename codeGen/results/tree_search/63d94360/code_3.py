MOD = 1000000007

def solve(N, K):
    # Initialize the DP array with zeros
    DP = [[0] * K for _ in range(N+1)]
    # Messi starts with the ball
    DP[0][0] = 1
    
    # Fill the DP array
    for i in range(1, N+1):
        for j in range(K):
            # Sum the number of ways from the previous pass excluding the current player
            DP[i][j] = sum(DP[i-1][k] for k in range(K) if k != j) % MOD
    
    # The answer is the number of ways Messi gets the ball on the N-th pass
    return DP[N][0]

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(solve(N, K))
