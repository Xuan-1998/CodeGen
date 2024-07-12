python
MOD = 1000000007

def solve_ball_passing(T, test_cases):
    results = []
    
    for N, K in test_cases:
        # dp[i][j] will store the number of ways to pass the ball exactly i times
        # such that the j-th player receives the ball on the i-th pass.
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        
        # Base case: Start with player 0 having the ball without any passes.
        dp[0][0] = 1
        
        for i in range(1, N + 1):
            for j in range(K + 1):
                dp[i][j] = 0
                for m in range(K + 1):
                    if m != j:
                        dp[i][j] = (dp[i][j] + dp[i-1][m]) % MOD
        
        results.append(dp[N][0])
    
    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    test_cases = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(T)]
    
    results = solve_ball_passing(T, test_cases)
    
    for result in results:
        print(result)

