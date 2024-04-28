def find_shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    m, n = len(S), len(T)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    uncommon_subsequence_length = m

    for i in range(m, -1, -1):
        if S[i] != T[uncommon_subsequence_length - 1]:
            return uncommon_subsequence_length
        uncommon_subsequence_length -= 1

    return -1


print(find_shortest_uncommon_subsequence())
