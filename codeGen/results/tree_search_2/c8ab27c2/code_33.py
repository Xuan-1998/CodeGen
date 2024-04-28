import sys

def uncommonFromS_and_T(S, T):
    dp = [[-sys.maxsize for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    uncommon_length = 0
    for i in range(len(S), 0, -1):
        if dp[i][0] > dp[i - 1][0]:
            uncommon_length += 1
            break

    return -1 if uncommon_length == 0 else len(S) - uncommon_length


# Example usage:
S = input()
T = input()

print(uncommonFromS_and_T(S, T))
