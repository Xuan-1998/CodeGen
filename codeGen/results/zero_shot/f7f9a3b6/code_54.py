def solve(s, a):
    n = len(s)
    b = [0] * 26
    for i in range(26):
        b[i] = a[0] + a[1] + ... + a[i-1]

    dp = [[0] * (n+1) for _ in range(n+1)]
    max_len = [[0] * (n+1) for _ in range(n+1)]

    dp[0][0] = 1
    for i in range(1, n+1):
        c = s[i-1]
        for j in range(min(i, 26), -1, -1):
            if ord(c) <= ord('a') + j:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])
                max_len[i][j] = max(max_len[i-1][j], len(s[:i]))
            else:
                dp[i][j] = dp[i-1][j]
                max_len[i][j] = max_len[i-1][j]

    ways = 0
    for k in range(n+1):
        if dp[n-1][k] > 0:
            ways = k
            break

    print(ways % (10**9 + 7))
    print(max_len[n-1][ways])
    print(1)
