MOD = 10**9 + 7

def solve():
    a, b = map(int, input().split())
    dp = {0: a ^ b}
    
    for i in range(1, 315160):
        if i % 2:
            b |= 1
        dp[i] = (dp.get(i - 1, a) ^ b)
        dp[i] %= MOD
    
    return sum(dp.values()) % MOD

print(solve())
