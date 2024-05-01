def findLCSLength(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif S[i - 1] != T[j - 1]:
                dp[i][j] = max(1, dp[i - 1][j]) if i > 0 else 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1

    result = m
    for i in range(m):
        for j in range(n):
            if S[i] != T[j]:
                result = min(result, dp[i][j])
                break

    return -1 if result == m else result


# Read input from stdin
S = input().strip()
T = input().strip()

print(findLCSLength(S, T))
