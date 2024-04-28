from sys import stdin, stdout

def uncommon_subsequence():
    S = stdin.readline().strip()
    T = stdin.readline().strip()

    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] != T[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

    return m + n - (dp[m][n] + 1)

print(uncommon_subsequence())
