def countWays(n):
    MOD = 10**9 + 7

    dp = {'' : 1}
    
    for i in range(1, n+1):
        dp[i] = {}
        for p in dp:
            if set(map(int, list(p))) | set(range(1, i+1)) == set(range(1, i+1)):
                continue
            k = (p[:p.index('1')] or '0').count('1')
            dp[i][p] = ((dp[i-k-1].get(p[:k], 0) + sum(dp[i-j-1][q] for j in range(k+1) for q in dp if q[:j] == p[:j])) % MOD)
    return sum(int(x) for x in dp[n]) % MOD

n = int(input())
print(countWays(n))
