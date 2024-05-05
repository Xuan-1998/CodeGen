from collections import defaultdict

def solve(t, s):
    n = len(s)
    m = len(t)

    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = 0

    for i in range(1, m + 1):
        for j in range(n + 1):
            if t[i - 1] not in s:
                dp[i][j] = dp[i - 1][j]
            else:
                for k in range(j - 1, -1, -1):
                    if t[i - 1:i + len(s[k]) - 1] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i - len(s[k])][k] + 1)

    res = []
    i, j = m, n
    while i > 0 and j > 0:
        if t[i - 1] not in s:
            i -= 1
        else:
            for k in range(j - 1, -1, -1):
                if t[i - 1:i + len(s[k]) - 1] == s[k]:
                    res.append((k, i - len(s[k]) + 1))
                    i -= len(s[k])
                    j = k
                    break

    return dp[m][n], '\n'.join(map(lambda x: f'{x[0]} {x[1]}', res)) if dp[m][n] != float('inf') else '-1'

t, n = map(str.strip, input().split('\n'))
strings = [s for s in (input().strip() for _ in range(int(n)))]

print(solve(t, strings))
