s = input().strip()
t = input().strip()

def shortest_uncommon_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    uncommon_length = m
    for i in range(m, -1, -1):
        if s[i:] not in t[:uncommon_length]:
            return uncommon_length
        uncommon_length -= 1

    return -1

print(shortest_uncommon_subsequence(s, t))
