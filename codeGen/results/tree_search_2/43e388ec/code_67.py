def solve():
    a, b = [int(x) for x in input().split()]
    MOD = 10**9 + 7
    dp = {0: 0}
    total_sum = 0

    for i in range(1, 315160):
        new_val = (dp.get(i-1, 0) + a ^ (b >> (i-1))) % MOD
        if i < len(bin(a)) or i < len(bin(b)):
            dp[i] = new_val
            total_sum = (total_sum + new_val) % MOD

    print(total_sum)

solve()
