def solve():
    t = int(input())
    MOD = 10**9 + 7

    dp = {(i+1, x^mask, y&mask): 0 for i in range(k) for mask in range(2**k)}

    for i in range(k-1, -1, -1):
        for mask in range(2**k):
            if (mask >> i) & 1:
                new_x = x ^ (mask << i)
                new_y = y & (mask << i)
                dp[(i+1, new_x, new_y)] += dp.get((i, x, y), 0)
                if i == 0 or (new_x >= new_y):
                    dp[(i+1, new_x, new_y)] = min(dp[(i+1, new_x, new_y)], MOD-1) + 1
    return dp[0, 0, (2**k)-1] % MOD

print(solve())
