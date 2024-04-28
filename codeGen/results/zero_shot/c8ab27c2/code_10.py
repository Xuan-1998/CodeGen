s = input()
t = input()

def uncommon_subsequence_length(s, t):
    s_len = len(s)
    t_len = len(t)

    dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]

    for i in range(s_len + 1):
        for j in range(t_len + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i - 1] != t[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1

    return s_len - dp[s_len][t_len]

print(uncommon_subsequence_length(s, t))
