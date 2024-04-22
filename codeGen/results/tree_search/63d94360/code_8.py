MOD = 1000000007

def number_of_ways(N, K):
    # Initialize the DP array with zeros
    DP = [[0 for _ in range(K)] for _ in range(N+1)]
    
    # Base case: Messi starts with the ball
    DP[0][0] = 1
    
    # Fill the DP array
    for i in range(1, N+1):
        for j in range(K):
            for k in range(K):
                if k != j:
                    DP[i][j] += DP[i-1][k]
                    DP[i][j] %= MOD
    
    # The answer is the number of ways Messi can receive the ball after N passes
    return DP[N][0]

# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(number_of_ways(N, K))
