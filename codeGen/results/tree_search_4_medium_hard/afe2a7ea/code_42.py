def solve(n):
    dp = {}
    dp[0, n+2] = 1
    for used_towers in range(1, n+1):
        for signals_left in range(n+1, 0, -1):
            if signals_left >= 0:
                dp[(used_towers, signals_left)] = (dp.get((used_towers-1, signals_left), 0) + dp.get((used_towers, signals_left-1), 0)) % (998244353)
    return dp[n, 0]

n = int(input())
print(solve(n))
