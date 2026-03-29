import math

mod = 998244353

def calculate_probability(n):
    dp = [[0] * (n + 1) for _ in range(n + 2)]
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i-1][0]
        for k in range(1, min(i, n - i) + 1):
            if k == 0:
                dp[i][k] = (n+2-i) * math.comb(n+2-i, i)
            else:
                dp[i][k] = sum(dp[j-1][k-1] * math.comb(i-j, k-1) for j in range(1, i))
    
    return dp[n][n]

n = int(input())
print(calculate_probability(n))
