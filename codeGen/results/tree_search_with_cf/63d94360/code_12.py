python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 1000000007
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        # Initialize dp table
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        
        # Fill the dp table
        for i in range(1, N + 1):
            for j in range(K + 1):
                dp[i][j] = sum(dp[i-1][m] for m in range(K + 1) if m != j) % MOD
        
        # The answer is the number of ways to pass the ball N times such that player 0 has it
        results.append(dp[N][0])
    
    # Print all results for each test case
    for result in results:
        print(result)


