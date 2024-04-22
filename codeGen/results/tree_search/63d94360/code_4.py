MOD = 1000000007

def calculate_ways(N, K):
    # Initialize the DP array with zeros
    DP = [[0 for _ in range(K)] for _ in range(N+1)]
    
    # Base case: 0 passes, Messi has the ball
    DP[0][0] = 1
    
    # Fill the DP array
    for i in range(1, N+1):
        for j in range(K):
            DP[i][j] = (sum(DP[i-1]) - DP[i-1][j]) % MOD
    
    # The answer is the number of ways to pass the ball N times and end up with Messi
    return DP[N][0]

# Read number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(calculate_ways(N, K))
