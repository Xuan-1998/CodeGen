def count_ways(m, N, arr):
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(m + 1)]
    
    # base case: there is exactly one way to form sum 0 using no elements
    dp[0][0] = 1
    
    for i in range(1, m + 1):
        for j in range(i, N + 1):
            if j < i:
                dp[i][j] = 0
            else:
                # consider using the current element 'x' as many times as possible
                x = arr[i - 1]
                ways_to_form_N_j = (dp[i - 1][j - x] or 0) + (dp[i - 1][j] if j > x else 0)
                dp[i][j] = ways_to_form_N_j % MOD
    
    return dp[m][N]
