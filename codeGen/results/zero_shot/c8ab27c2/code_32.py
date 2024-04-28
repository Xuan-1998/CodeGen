s = input().strip()
t = input().strip()

def find_length(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    for i in range(m, -1, -1):
        if all(s[i - k] != t[j - k] for k in range(min(i, len(t)))):
            return i

    return -1

print(find_length(s, t))
