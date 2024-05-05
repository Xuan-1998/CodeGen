def max_bitwise_or(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if s[i] == '1' and s[j - 1] == '1':
                dp[i][j] = max(dp[i + 1][j - 1], (int(s[:i+1], 2) | int(s[i:j], 2)) << (i - j))
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return bin(max([dp[i][n] for i in range(n)]))[2:]

s = input()
print(max_bitwise_or(s))

