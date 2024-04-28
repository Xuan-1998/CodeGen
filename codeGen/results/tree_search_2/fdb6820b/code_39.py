def count_ways(arr, N):
    MOD = 10**9 + 7
    dp = {0: 1}
    
    for i in range(1, N+1):
        if i not in dp:
            continue
        
        ways_to_form_i = dp[i]
        for num in arr:
            j = i - num
            if j >= 0 and j in dp:
                ways_to_form_i += dp[j]
        
        dp[i] = ways_to_form_i % MOD
    
    return dp[N]
