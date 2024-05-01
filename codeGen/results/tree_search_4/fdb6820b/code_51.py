def count_ways(m, N, arr):
    MOD = 10**9 + 7

    dp = [[0] * (N+1) for _ in range(m+1)]
    
    # Initialize the base case: there is only one way to form sum 0 with no elements.
    dp[0][0] = 1

    for i in range(1, m+1):
        for j in range(N+1):
            if arr[i-1] <= j:
                # Calculate the number of ways to form sum j by adding the current element and previous sums.
                dp[i][j] = (dp[i-1][j-arr[i-1]] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]

    return dp[m][N]
