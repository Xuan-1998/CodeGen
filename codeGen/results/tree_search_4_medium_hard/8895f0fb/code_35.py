def expected_carries(N):
    dp = [[0.0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: no carry when adding two empty numbers
    dp[0][0] = 0
    
    for n in range(1, N + 1):
        for m in range(1, N + 1):
            if n > 0 and m > 0:
                # Both digits are not zero: calculate the expected carry
                dp[n][m] = (dp[n-1][m-1] + (n >= 10 or m >= 10)) / ((N-n) * (N-m))
            elif n == 0:
                # Only B has digits, so only consider B's last digit
                dp[n][m] = (dp[0][m-1] + (m >= 10)) / (N-m)
            elif m == 0:
                # Only A has digits, so only consider A's last digit
                dp[n][m] = (dp[n-1][0] + (n >= 10)) / (N-n)
    
    return dp[N][N]
