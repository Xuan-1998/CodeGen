def shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    def common_subsequence(i, j):
        if i == 0 or j == 0:
            return False
        return S[i - 1] != T[j - 1] and dp[i - 1][j] or dp[i][j - 1]

    for i in range(m + 1):
        for j in range(n + 1):
            if common_subsequence(i, j):
                dp[i][j] = True
            else:
                dp[i][j] = False

    res = float('inf')
    for i in range(m + 1):
        for j in range(n + 1):
            if not dp[i][j]:
                res = min(res, m - i if i < m else n - j)

    return -1 if res == float('inf') else res
