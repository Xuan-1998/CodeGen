def solve():
    t = int(input())
    MOD = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(k+1)]

        for i in range(1, k+1):
            for mask in range(1 << i):
                if i > k:
                    dp[i][mask] = 1
                else:
                    for v in range(mask+1):
                        if ((v & mask) <= mask) and (v <= v ^ mask):
                            dp[i][mask] += dp[i-1][v]
                    dp[i][mask] %= MOD

        print(sum(dp[k]) % MOD)

solve()
