def min_recolors(s):
    n = len(s)
    dp = [[float('inf')] * 3 for _ in range(n + 1)]

    # Base case: a garland of length 0 or 1 doesn't need recoloring
    dp[0][s[0]] = dp[1][s[1]] = 0

    for i in range(2, n + 1):
        for j in [0, 1, 2]:  # red (0), green (1), blue (2)
            if i == 2:
                dp[i][j] = 1
            else:
                for k in [0, 1, 2]:
                    if j != k:  # different color from the last one
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + (s[i-1] == str(k)))
    return dp[n-1][int(s[-1])] + 1

n, s = map(str, input().split())
print(min_recolors(s))
