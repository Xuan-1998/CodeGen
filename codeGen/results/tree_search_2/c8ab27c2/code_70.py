import sys

def shortest_uncommon_subsequence(S, T):
    memo = {(-1, -1): None}
    dp = [[-1] * (len(T) + 1) for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = min(dp[i - 1][k] for k in range(j + 1)) + 1
            else:
                dp[i][j] = dp[i - 1][j]

    return max(0, dp[-1][-1])

# Read input from standard input
S = input().strip()
T = input().strip()

print(shortest_uncommon_subsequence(S, T))
