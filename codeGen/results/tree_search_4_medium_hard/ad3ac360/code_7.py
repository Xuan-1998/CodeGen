def min_cuts(s):
    n = len(s)
    dp = [[False] * (n+1) for _ in range(n+1)]

    # Initialize first row and column to True
    for i in range(n+1):
        dp[i][0] = dp[0][i] = True

    for i in range(1, n+1):
        for j in range(i, -1, -1):
            if s[i-1] == s[j]:
                dp[i][j] = dp[i-1][j+1]
            else:
                dp[i][j] = False

    cuts = 0
    i, j = n-1, n-1
    while i > 0 and j >= 0:
        if not dp[i][j]:
            cuts += 1
            i -= 1
            j = i
        else:
            i -= 1
            j -= 1

    return cuts
