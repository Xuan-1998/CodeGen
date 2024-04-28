import sys

def uncommon_subsequences(S, T):
    m, n = len(S), len(T)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = (dp[i - 1][j] or dp[i][j - 1])

    ans = m
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if not dp[i][j]:
                ans = min(ans, i)
                break
        else:
            continue
        break

    return ans if ans != m else -1

S = input().strip()
T = input().strip()

print(uncommon_subsequences(S, T))
