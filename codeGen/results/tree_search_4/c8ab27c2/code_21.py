===BEGIN CODE===
def uncommon_subsequence_length(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] != t[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = 0

    return dp[-1][-1]

s = input().strip()
t = input().strip()

print(uncommon_subsequence_length(s, t))
===END CODE===
