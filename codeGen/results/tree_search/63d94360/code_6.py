MOD = 1000000007

def solve(N, K):
    # Initialize DP array with zeros
    DP = [[0] * K for _ in range(N+1)]
    
    # Base case: 0 passes, ball with Messi
    DP[0][0] = 1
    
    # Fill the DP array
    for i in range(1, N+1):
        # When ball is passed to Messi
        DP[i][0] = sum(DP[i-1][1:]) % MOD
        # When ball is passed to other players
        for j in range(1, K):
            DP[i][j] = (DP[i-1][0] + sum(DP[i-1][1:j]) + sum(DP[i-1][j+1:])) % MOD
    
    # The answer is the number of ways to pass the ball N times, ending with Messi
    return DP[N][0]

# Read the number of test cases
T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(solve(N, K))
