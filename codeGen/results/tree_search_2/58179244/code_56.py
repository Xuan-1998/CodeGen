def min_recolors(s):
    n = len(s)
    dp = [[0] * 3 for _ in range(n)]

    for i in range(1, n):
        c1, c2 = ord(s[i-1]) - ord('R'), ord(s[i]) - ord('R')
        if c1 == c2:
            dp[i][c1] = dp[i-1][c1] + 1
        else:
            dp[i][c1] = min(dp[i-1][0], dp[i-1][1]) + (c1 == 0)
            dp[i][c2] = min(dp[i-1][0], dp[i-1][1]) + (c2 == 0)

    r, c1 = n-1, ord(s[n-1]) - ord('R')
    res = []

    for i in range(n):
        if dp[i][c1] < dp[i][0]:
            c1 = 0
        elif dp[i][c1] > dp[i][1]:
            c1 = 1

        res.append(['RGB'][c1])

    return str(r) + '\n' + ''.join(res)
