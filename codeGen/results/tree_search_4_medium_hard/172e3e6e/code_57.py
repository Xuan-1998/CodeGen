def good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = {0: 1}
    
    for i in range(1, n):
        dp[i] = 0
        for j in range(i):
            if a[i] % a[j] == 0:
                dp[i] += dp[j]
        dp[i] %= (10**9 + 7)
    
    return sum(dp.values())
