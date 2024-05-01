from collections import defaultdict

def find_shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    n, m = len(S), len(T)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    S_count = defaultdict(int)
    T_count = defaultdict(int)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if S_count[S[i - 1]] > 0 and T_count[T[j - 1]] > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
                elif S_count[S[i - 1]] > 0:
                    dp[i][j] = dp[i - 1][j]
                elif T_count[T[j - 1]] > 0:
                    dp[i][j] = dp[i][j - 1]

            S_count[S[i - 1]] += (dp[i][j] == dp[i - 1][j])
            T_count[T[j - 1]] += (dp[i][j] == dp[i][j - 1])

    return dp[n][m] - 1

print(find_shortest_uncommon_subsequence())
