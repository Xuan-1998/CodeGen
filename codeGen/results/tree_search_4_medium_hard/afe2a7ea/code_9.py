def solve():
    n = int(input())
    MOD = 998244353
    dp = [[0]*(n+2) for _ in range(n+2)]
    
    # base case: no towns have towers
    for i in range(n+2):
        dp[i][0] = 1
    
    for j in range(1, n+2):
        for i in range(j-1, -1, -1):
            if (i+j)%2 == 1:
                continue
            for k in range(i+1):
                dp[j][k+1] = (dp[j][k+1] + dp[i][k]) % MOD
    
    return dp[0][n+1]

print(solve())
