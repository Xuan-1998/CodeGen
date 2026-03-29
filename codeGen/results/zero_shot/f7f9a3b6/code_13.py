def split_string(s, a):
    n = len(s)
    count = [0] * 26
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    max_count = max(a)
    min_count = min(a)

    dp = [[[] for _ in range(max_count + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, max_count) + 1):
            if count[ord(s[i - 1]) - ord('a')] > a[ord(s[i - 1]) - ord('a')]:
                dp[i][j] = dp[i - 1][j]
            else:
                if len(dp[i - 1][j - 1]) + 1 <= j and count[ord(s[i - 1]) - ord('a')] <= a[ord(s[i - 1]) - ord('a')]:
                    dp[i][j] = dp[i - 1][j - 1] + [s[:i]]
                else:
                    dp[i][j] = dp[i - 1][j]
    
    ways = len(dp[n][max_count])
    max_length = max(len(substring) for substring in dp[n][max_count])
    min_substrings = ways
    return ways % (10**9 + 7), max_length, min_substrings % (10**9 + 7)
