import sys

def color_text(t, n, s):
    m = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, min(i, n) + 1):
            if all(c == 'R' for c in t[:i]):
                dp[i][j] = dp[i - 1][j]
            else:
                for k in range(n):
                    used = [0] * (n + 1)
                    used[k] = 1
                    steps = dp[i - len(s[k])][j - 1] if j > 0 else sys.maxsize
                    for p in range(i - len(s[k]), i):
                        if t[p] == 'R':
                            steps -= 1
                    dp[i][j] = min(dp[i][j], steps + (dp[i - len(s[k])][j] if dp[i - len(s[k])][j] != sys.maxsize else 0))

    if dp[m][n] > m:
        return -1

    used_strings = []
    i, j = m, n
    while j > 0:
        for k in range(n):
            if not any(used_strings) or dp[i][j] == dp[i - len(s[k])][j - 1]:
                used_strings.append(k)
                i -= len(s[k])
                j -= 1
                break

    return dp[m][n], used_strings
