def solve(n, s, a):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp_length = [[0] * (n + 1) for _ in range(n + 1)]

    dp[0][n] = 1

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if s[i - 1].isalpha() and a[ord(s[i - 1].lower()) - ord('a')] >= j - i:
                dp[i][j] = (dp[i - 1][i] + dp[i][j]) % (10**9 + 7)
                dp_length[i][j] = max(dp_length[i - 1][i], j - i)
            else:
                dp[i][j] = 0

    ways_to_split = dp[0][n]
    longest_substring = max(max(row) for row in dp_length)

    min_splits = ways_to_split
    if ways_to_split > 0:
        min_splits //= ways_to_split + 1
        min_splits += 1

    print(ways_to_split % (10**9 + 7))
    print(longest_substring)
    print(min_splits)
