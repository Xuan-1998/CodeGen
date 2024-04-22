MOD = 1000000007

def solve(N, K):
    # Initialize the DP array with zeroes
    DP = [[0 for _ in range(K)] for _ in range(N+1)]
    # Messi has the ball initially
    DP[0][0] = 1

    # Fill the DP array
    for i in range(1, N+1):
        for j in range(K):
            # The ball can come from any other player
            for k in range(K):
                if k != j:
                    DP[i][j] += DP[i-1][k]
                    DP[i][j] %= MOD

    # The answer is the number of ways Messi can receive the ball after N passes
    return DP[N][0]

# Read the number of test cases
T = int(input().strip())
for _ in range(T):
    # Read N and K for each test case
    N, K = map(int, input().strip().split())
    # Print the result
    print(solve(N, K))
