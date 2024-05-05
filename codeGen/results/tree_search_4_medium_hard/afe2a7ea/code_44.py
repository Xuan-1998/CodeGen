MOD = 998244353

def dp(towers):
    if towers == -1:
        return 1
    if memo[towers] != -1:
        return memo[towers]
    
    res = 0
    for i in range(1, towers + 1):
        if (towers + 1) % i == 0:
            res += dp(towers - 1)
    memo[towers] = res % MOD
    return res

n = int(input())
memo = [-1] * (2 * n + 2)
print(dp(n))
