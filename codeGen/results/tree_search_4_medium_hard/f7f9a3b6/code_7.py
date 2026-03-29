def solve(n, s, a):
    mod = 10**9 + 7

    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][n-1] = 1

    for i in range(1, n):
        for j in range(i, n):
            count = sum((a[ord(c)-97]) for c in s[i:j+1])
            dp[i][j] = sum(dp[k-1][i-1] * (count >= k) for k in range(i+1, j+2))

    ways = dp[0][n-1]
    longest_substring_length = max(len(s[i:j+1]) for i in range(n) for j in range(i+1, n) if all(count >= k for k in range(i+1, j+2)))
    min_substrings = sum(1 for _ in range(n) if dp[0][i-1] > 0 and (dp[i][n-1] == 0 or i == n-1))

    print(ways % mod)
    print(longest_substring_length)
    print(min_substrings)
