MOD = 1000000007

def calculate_ways(N, K):
    # Initialize the DP table with zeros
    dp = [[0 for _ in range(K)] for _ in range(N+1)]
    
    # Base case: Messi starts with the ball
    dp[0][0] = 1
    
    # Populate the DP table
    for i in range(1, N+1):
        for j in range(K):
            for k in range(K):
                if k != j:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= MOD
    
    # The answer is the number of ways Messi can receive the ball after N passes
    return dp[N][0]

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N, K = map(int, input().split())
    print(calculate_ways(N, K))
