S = input()
T = input()

def find_shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    uncommon_length = float('inf')

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            if dp[i][j] < uncommon_length:
                uncommon_length = dp[i][j]

    return uncommon_length

print(find_shortest_uncommon_subsequence(S, T))
