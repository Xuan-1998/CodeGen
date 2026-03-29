def solve():
    n = int(input())
    MOD = 998244353

    dp = [[0] * (1 << (n + 2)) for _ in range(n + 2)]

    dp[0][0] = 1

    for used_towers in range(1, n + 2):
        for signal_mask in range((1 << (n + 2))):
            if not any((signal_mask >> i) & 1 for i in range(1, n + 1)):
                dp[used_towers][signal_mask] = sum(dp[i][j ^ signal_mask] for i in range(max(0, used_towers - 1), used_towers))
        dp[used_towers][0] = (dp[used_towers][0] * (n + 2)) % MOD

    result = dp[-1][-1]
    print((result * pow(n + 2, -1, MOD)) % MOD)

if __name__ == "__main__":
    solve()
