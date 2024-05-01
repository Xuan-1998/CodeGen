def solve():
    a, b = map(int, input().split())
    
    dp = {0: 0}
    for i in range(1, 314160):
        dp[i] = (dp.get(i-1, 0) + ((a ^ (b << (i-1)))) % (10**9+7))
    
    return sum(dp.values()) % (10**9+7)

print(solve())
