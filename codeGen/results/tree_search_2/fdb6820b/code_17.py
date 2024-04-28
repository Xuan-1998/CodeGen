def numWays(nums, n):
    MOD = 10**9 + 7
    memo = {0: 1}
    
    for i in range(n+1):
        if i not in memo:
            memo[i] = 0
        for j in nums:
            k = i - j
            if k >= 0 and k in memo:
                memo[i] = (memo[i] + memo[k]) % MOD
    
    return memo[n]
