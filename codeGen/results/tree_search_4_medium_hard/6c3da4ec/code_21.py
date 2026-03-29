def maxOrSubstrings():
    n = int(input())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if s[j - 1] == '0':
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j])
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1] | (1 << (s[j - 2] - '0')))

    return max(max(row) for row in dp)
