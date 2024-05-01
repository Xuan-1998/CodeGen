def shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i + 1

    for j in range(n + 1):
        dp[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                if not is_subsequence(S[:i], T):
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i][j]

    return dp[m][n]


def is_subsequence(s, t):
    it = iter(t)
    for char in s:
        try:
            if char != next(it):
                return False
        except StopIteration:
            return False
    return True


# Example usage:
S = input()
T = input()
print(shortest_uncommon_subsequence(S, T))
