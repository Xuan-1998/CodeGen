MOD = 1000000007

def calculate_ways(N, K):
    # Initialize the DP array
    DP = [[0] * K for _ in range(N+1)]
    DP[0][0] = 1  # Base case: Messi starts with the ball

    for i in range(1, N+1):
        # Calculate DP[i][0], the number of ways Messi can receive the ball
        DP[i][0] = sum(DP[i-1][1:]) % MOD
        for j in range(1, K):
            # Calculate DP[i][j], the number of ways the j-th player can receive the ball
            DP[i][j] = (DP[i-1][0] + sum(DP[i-1][1:j]) + sum(DP[i-1][j+1:])) % MOD

    return DP[N][0]

# Read the number of test cases
T = int(input())
for _ in range(T):
    # Read N and K for each test case
    N, K = map(int, input().split())
    # Print the number of ways modulo 1000000007
    print(calculate_ways(N, K))
