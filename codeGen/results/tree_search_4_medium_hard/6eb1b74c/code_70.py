def solve(t, S):
    n = len(S)
    m = float('inf')
    dp = [[False] * (len(t) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = True
        for j in range(1, len(t) + 1):
            if t[j - 1] in S[i - 1]:
                dp[i][j] = dp[i][j - 1] or (dp[i - 1][j - len(S[i - 1])] and True)
            else:
                dp[i][j] = dp[i][j - 1]

    if not dp[n][len(t)]:
        return -1

    m = max(len(s) for s in S)
    steps = []
    p = len(t)
    for _ in range(m + 1):
        for i in range(n, 0, -1):
            if t[p - len(S[i - 1]):p] == S[i - 1]:
                steps.append((i, p - len(S[i - 1])))
                p -= len(S[i - 1])
                break
        else:
            return -1

    print(m)
    for w, p in steps:
        print(w, p)
