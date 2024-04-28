from sys import stdin

def uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i-1] not in T[:j]:
                dp[i][j] = i
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])

    ans = -1
    for i in range(m, -1, -1):
        if S[i:] not in T:
            ans = i + 1
            break

    return ans


S, T = [line.strip() for line in stdin]
print(uncommon_subsequence(S[0], T[0]))
