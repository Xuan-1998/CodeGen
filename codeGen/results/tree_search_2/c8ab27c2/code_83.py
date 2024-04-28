import sys

def uncommon_subsequence_length():
    S = input().strip()
    T = input().strip()

    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the minimum length of shortest uncommon subsequence in S[:i+1] and T[:j+1]
    min_length = float('inf')
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            if dp[i][j] == 0:
                continue
            length = dp[i][j]
            while i > 0 and S[i - 1] != T[j - 1]:
                i -= 1
                j -= 1
                length += 1
            min_length = min(min_length, length)

    if min_length == float('inf'):
        print(-1)
    else:
        print(min_length)

uncommon_subsequence_length()
