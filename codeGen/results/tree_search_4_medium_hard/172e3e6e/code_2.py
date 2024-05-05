def good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [[0] * (i+1) for i in range(n)]
    dp[0][0] = 1
    
    for i in range(1, n):
        for k in range(1, min(a[i], i)+1):
            if a[i] % k == 0:
                dp[i][k] = (dp[i-1][1] + 1) if k == 1 else (dp[i-1][k] + dp[i-1][k//k]) % MOD
            else:
                dp[i][k] = 0
    
    total_good_subsequences = sum(dp[-1])
    
    print(total_good_subsequences % MOD)
