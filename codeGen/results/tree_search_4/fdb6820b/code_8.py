def ways_to_form_N():
    m, N = map(int, input().split())
    array = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [[0] * (N + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = 1
    
    for i in range(1, m + 1):
        for j in range(N + 1):
            if array[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - array[i - 1]]) % MOD
    
    return dp[m][N]

print(ways_to_form_N())
