def min_changes(s, k):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill up the dp array
    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if s[i - 1] == 'RGB'[j % 3]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + 1)

    # Find the minimum number of changes needed to make a substring of length k equal to a substring of 'RGBRGBRGB...'
    for i in range(k, n + 1):
        if s[i - 1] != 'RGB'[i % 3]:
            return dp[i][k]

    return dp[n][k]

while True:
    try:
        n, k = map(int, input().split())
        s = input()
        print(min_changes(s, k))
    except EOFError:
        break
