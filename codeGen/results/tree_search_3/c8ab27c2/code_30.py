import sys

def uncommon_subsequences(S, T):
    n = len(S)
    m = len(T)

    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(1, min(i, m) + 1):
            if S[i - 1] == T[k - 1]:
                dp[i][k] = dp[i - 1][k - 1]
            else:
                dp[i][k] = max(dp[i - 1][k], dp[i][k - 1])

    result = -1
    for i in range(n, -1, -1):
        if not any(S[j:i] in T for j in range(i)):
            result = i
            break

    return result

# Read input from standard input
S = input().strip()
T = input().strip()

print(uncommon_subsequences(S, T))
