def expected_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N+1) for _ in range(N+1)]
        
        # Base cases
        for k in range(N+1):
            dp[0][k] = 0
        
        for n in range(1, N+1):
            for k in range(N+1):
                if n == 0:
                    continue
                
                max_value = max(9 - (10 ** (N - n)), int((10 ** (N - n + 1)) / 11))
                
                dp[n][k] = (dp[n-1][max(k, max_value)] if k > 0 else 
                            dp[n-1][0]) + (1 if k > 0 and max_value >= 9 else 0)
        
        total_carries = sum(dp[N][i] for i in range(N+1))
        print(total_carries / ((10 ** N) * (10 ** N)))

expected_carries()
