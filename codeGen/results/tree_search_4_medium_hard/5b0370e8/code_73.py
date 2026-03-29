def and_xor_count():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [0] * (1 << k)
        dp[0] = 1

        for i in range(2**k - 1, -1, -1):
            j = i ^ ((1 << k) - 1)
            if i & j:
                dp[i] = sum(dp[x] for x in range(j + 1, (1 << k)))
            else:
                dp[i] = sum(dp[x] * 2**(k - bit) for x in range(i + 1, (1 << k))) % (10**9 + 7)
        print((dp[-1]) % (10**9 + 7))

and_xor_count()
