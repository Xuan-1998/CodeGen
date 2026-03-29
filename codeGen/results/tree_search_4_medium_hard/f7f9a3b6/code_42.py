def split_string(s, a):
    MOD = 10**9 + 7
    n = len(s)
    max_a = max(a)

    dp = [[0] * (max_a + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(1, min(i, a[25]) + 1):
            if i < 1 or k > max_a:
                dp[i][k] = 0
            else:
                dp[i][k] = sum(dp[i - j][j] * (a[j - 1] + 1) for j in range(1, min(i, a[25]) + 1))

    ways_to_split = dp[n][max_a]
    longest_substring = max((dp[i][k] for i in range(n + 1)), key=lambda x: x[0])[0]

    min_substrings = min((k for k in range(1, ways_to_split + 1)), key=lambda x: (ways_to_split - x) * 2)

    print(ways_to_split % MOD)
    print(longest_substring)
    print(min_substrings)
