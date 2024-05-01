import sys

def uncommon_subsequence(S, T):
    # Find the LCS of S and T using dynamic programming
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the minimum value in the DP array that's not equal to the LCS length
    min_length = sys.maxsize
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            if dp[i][j] != len(LCS(S, T)):
                min_length = min(min_length, len(S) - i + len(T) - j)

    return max(0, min_length)


def LCS(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                continue
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the DP array
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if S[i - 1] == T[j - 1]:
            result.append(S[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))


if __name__ == "__main__":
    S, T = input().split()
    print(uncommon_subsequence(S, T))
