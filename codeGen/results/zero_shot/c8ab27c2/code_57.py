S = input().strip()
T = input().strip()

def find_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                continue
            elif j == 0:
                continue
            elif S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    uncommon_subsequence_length = m
    for i in range(m):
        if dp[m - 1 - i][n] >= m - i:
            uncommon_subsequence_length = m - i
            break

    print(uncommon_subsequence_length)
