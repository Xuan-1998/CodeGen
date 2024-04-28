s = input().strip()
t = input().strip()

def find_shortest_uncommon_subsequence():
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    uncommon_length = n - dp[n][m]
    return -1 if uncommon_length < 0 else uncommon_length

print(find_shortest_uncommon_subsequence())
