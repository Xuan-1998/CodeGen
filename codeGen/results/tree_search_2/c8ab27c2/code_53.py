def find_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    m = len(S)
    n = len(T)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return m if dp[m][n] == 0 else -1

print(find_uncommon_subsequence())
