def findShortestSubArray(S: str, T: str) -> int:
    n = len(S)
    m = len(T)

    dp = [[-1] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            if S[i - 1] != T[j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = -1

    shortest_length = n + 1
    for i in range(n + 1):
        for j in range(m + 1):
            if dp[i][j] == -1 and (i == n or j == m or dp[i + 1][j] < 0 or dp[i][j + 1] < 0):
                shortest_length = min(shortest_length, i + 1)

    return shortest_length - 1 if shortest_length != n + 1 else -1
