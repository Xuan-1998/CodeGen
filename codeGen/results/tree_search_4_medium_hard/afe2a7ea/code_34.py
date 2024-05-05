def solve():
    n = int(input())
    mod = 998244353
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j]
            if i % (j + 1) == 0:
                dp[i] %= mod
    return dp[n]
