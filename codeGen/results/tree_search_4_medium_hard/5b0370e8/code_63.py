def and_or_xor():
    t = int(input())
    mod = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            x = int(input())
            for j in range((1 << k) - 1, x - 1, -1):
                if j & x:
                    break
                dp[i][j] += (dp[i - 1][j ^ x] % mod)

        print(dp[n][0] % mod)
