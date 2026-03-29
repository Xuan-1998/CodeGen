def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 1000000007
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        # dp[i][j] means the number of ways to pass the ball i times such that player j has the ball
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        
        # Initial state: 0 passes, player 0 has the ball
        dp[0][0] = 1
        
        # Fill the dp table
        for i in range(1, N + 1):
            for j in range(K + 1):
                dp[i][j] = sum(dp[i-1][m] for m in range(K + 1) if m != j) % MOD
        
        # The result for this test case is dp[N][0] since player 0 should have the ball last
        results.append(dp[N][0])
    
    # Print all results for each test case
    for result in results:
        print(result)


