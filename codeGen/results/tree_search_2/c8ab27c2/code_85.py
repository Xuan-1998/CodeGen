def shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] != T[j - 1]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1]
            if i > 0 and dp[i][j] == 0:
                dp[i][j] = dp[i-1][j]

    return len(S) - dp[-1][-1]

print(shortest_uncommon_subsequence())
