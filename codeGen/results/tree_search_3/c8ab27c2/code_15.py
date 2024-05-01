def shortest_common_subsequence(S, T):
    m = len(S)
    n = len(T)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the minimum length of a subsequence that is not present in T
    for i in range(m, -1, -1):
        if all(x != y for x, y in zip(S[:i], T)):
            return i

    return -1


if __name__ == "__main__":
    S = input().strip()
    T = input().strip()

    result = shortest_common_subsequence(S, T)
    print(result)
