python
MOD = 1000000007

def solve_ball_passing(T, test_cases):
    results = []
    
    for N, K in test_cases:
        # Initialize dp table
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        
        # Base case: At the 0th pass, only player P (we assume P is player 0) has the ball
        dp[0][0] = 1
        
        # Fill the dp table
        for i in range(1, N + 1):
            for j in range(K + 1):
                dp[i][j] = sum(dp[i-1][m] for m in range(K + 1) if m != j) % MOD
        
        # The result for this test case is the number of ways to pass the ball N times to player 0
        results.append(dp[N][0])
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
test_cases = [(int(data[2*i+1]), int(data[2*i+2])) for i in range(T)]

# Solve the problem for each test case
results = solve_ball_passing(T, test_cases)

# Output the results
for result in results:
    print(result)

