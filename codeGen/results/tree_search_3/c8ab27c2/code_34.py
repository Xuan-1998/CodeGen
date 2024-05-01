def shortest_uncommon_subsequence():
    m, n = [int(x) for x in input().split()]
    s = input().strip()
    t = input().strip()

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    lcs_len = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                lcs_len = dp[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    uncommon_subsequence_len = min(m, n) - lcs_len
    print(uncommon_subsequence_len)

shortest_uncommon_subsequence()
