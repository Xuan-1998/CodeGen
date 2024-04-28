s = input()
t = input()

def uncommon_subsequence_length(s, t):
    s_len = len(s)
    t_len = len(t)

    dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]
    res = s_len

    for i in range(1, s_len + 1):
        for j in range(1, t_len + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for i in range(1, s_len + 1):
        if res > i and not is_subsequence(s[:i], t):
            return i

    return -1


def is_subsequence(s, t):
    t_index = 0
    for c in s:
        while t_index < len(t) and t[t_index] != c:
            t_index += 1
        if t_index == len(t):
            return False
        t_index += 1
    return True

print(uncommon_subsequence_length(s, t))
