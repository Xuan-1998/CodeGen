def uncommonFromS(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

    uncommon_len = 0
    i, j = len(s), len(t)
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            i -= 1
            j -= 1
        elif dp[i - 1][j] < dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    uncommon_len = len(s) - i

    return uncommon_len if uncommon_len > 0 else -1


s = input()
t = input()

print(uncommonFromS(s, t))
