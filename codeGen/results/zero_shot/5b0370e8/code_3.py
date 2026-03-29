def count_arrays():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            and_mask = 0
            xor_mask = 0
            for j in range(i):
                x = int(input())
                and_mask |= (x & ((1 << k) - 1))
                xor_mask ^= x
            dp[i][and_mask] += dp[i-1][0]
        res = sum(dp[n])
        print((res + 7) % (10**9 + 7))

count_arrays()
