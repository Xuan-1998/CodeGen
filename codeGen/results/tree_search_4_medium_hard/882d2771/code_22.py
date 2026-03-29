def solve():
    t, l, r = map(int, input().split())
    MOD = 10**9 + 7
    dp = [0] * (r - l + 2)
    
    for i in range(1, r - l + 2):
        for j in range(l, i):
            for k in range(max(l, j), min(i, r)):
                if k - l + 1 > 0:
                    dp[i] = min(dp[i], dp[j] + dp[k - l])
    
    return (t * sum([dp[i] for i in range(l, r+1)]) % MOD)

print(solve())
