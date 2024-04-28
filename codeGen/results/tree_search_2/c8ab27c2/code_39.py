def uncommon_subsequences(S, T):
    m, n = len(S), len(T)
    common = [[0] * (n + 1) for _ in range(m + 1)]
    uncommon = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                common[i][j] = 0
            elif S[i - 1] == T[j - 1]:
                common[i][j] = common[i - 1][j - 1] + 1
            else:
                common[i][j] = max(common[i - 1][j], common[i][j - 1])
            if i > 0 and j > 0 and S[i - 1] != T[j - 1]:
                uncommon[i][j] = min(uncommon[i - 1][j], uncommon[i][j - 1])

    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and j > 0:
                uncommon[i][j] = min(uncommon[i][j], 1)

    answer = float('inf')
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and j > 0:
                answer = min(answer, uncommon[i][j])

    return -1 if answer == float('inf') else m + n - answer
