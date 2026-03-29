def expected_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0.0 for _ in range(N+1)] for _ in range(N+1)]
        
        # base case: when one or both numbers have only one digit
        for i in range(2, 10):  # 2 to 9
            total_carries = sum((i-1)//10) * (i//10) + sum((i-1)%10) % 10
            dp[0][i] = total_carries / (i+1)
        
        for i in range(N, -1, -1):
            for k in range(min(i+1, N), -1, -1):
                if k > 0:
                    dp[i][k] = (dp[i-1][k-1] + dp[i-k][k]) / (i+1)
        
        total_expected_carries = sum([sum(dp[i]) for i in range(N+1)])
        print(total_expected_carries)
