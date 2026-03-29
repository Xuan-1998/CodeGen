def solve(n, s, a):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    max_len = [0] * 27

    # Calculate max_len[i]
    for i in range(26):
        max_len[i] = min(a[i], n // 26)

    # Initialize dp[0][j] and dp[i][0]
    for j in range(n + 1):
        dp[0][j] = 1
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill up the dp table
    for i in range(1, n + 1):
        for j in range(1, min(i, 27)):
            for k in range(max_len[j - 1] + 1):
                if i >= k * (j - 1) and s[i - 1].isalpha() == (j - 1) % 26:
                    dp[i][j] = (dp[i - k * (j - 1)][j - 1] + dp[k * (j - 1)][j]) % (10**9 + 7)

    # Calculate the result
    ways = dp[n][27]
    max_len_substr = max(max_len)
    min_substrings = n // max_len_substr

    print(ways)
    print(max_len_substr)
    print(min_substrings)
