def palindromic_partitions(S):
    dp = [[[] for _ in range(len(S) + 1)] for _ in range(len(S) + 1)]

    for i in range(len(S) + 1):
        dp[i][i] = [[S[i]]]

    for j in range(1, len(S)):
        for i in range(j):
            if S[i] == S[j]:
                left_partition = dp[i][i-1] if i > 0 else []
                right_partition = dp[i+1][j]
                partitions = [left_partition + [''] + right_partition]
                dp[i][j].extend([p for p in partitions])
            else:
                dp[i][j].extend(dp[i][k] + [['', S[k]]] + dp[k+1][j] for k in range(i, j))
    return [p for p in dp[0][-1]]
