import sys

def shortest_uncommon_subsequence(S, T):
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] != T[j - 1]:
                dp[i][j] = (dp[i - 1][j] or dp[i][j - 1]) + 1
            else:
                dp[i][j] = 0

    shortest_length = sys.maxsize

    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] != T[j]:
                length = i + j - (dp[i][j] or 0)
                shortest_length = min(shortest_length, length)

    return -1 if shortest_length == sys.maxsize else shortest_length

S = input()
T = input()

print(shortest_uncommon_subsequence(S, T))
