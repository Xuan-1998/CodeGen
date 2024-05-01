import sys
from functools import lru_cache

def uncommon_subsequence_length(S, T):
    # Find the length of LCS
    @lru_cache(None)
    def lcs_length(i, j):
        if i == 0 or j == 0:
            return 0
        if S[i - 1] == T[j - 1]:
            return 1 + lcs_length(i - 1, j - 1)
        else:
            return max(lcs_length(i - 1, j), lcs_length(i, j - 1))

    # Find the length of LCS
    S_len = len(S)
    T_len = len(T)

    lcs = [[0] * (T_len + 1) for _ in range(S_len + 1)]

    for i in range(1, S_len + 1):
        for j in range(1, T_len + 1):
            if S[i - 1] == T[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    # The length of the shortest uncommon subsequence is the minimum between S_len and T_len, minus the length of LCS
    return min(S_len, T_len) - lcs[S_len][T_len]

# Get input from standard input
S = input().strip()
T = input().strip()

print(uncommon_subsequence_length(S, T))
