s = input().strip()
t = input().strip()

def find_shortest_uncommon_subsequence(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    length = len(s) - dp[-1][-1]
    return length if length > 0 else -1

print(find_shortest_uncommon_subsequence(s, t))
