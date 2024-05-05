from sys import stdin

def lex_smallest_string(s, k):
    if k > len(s):
        return s * (k // len(s) + 1)
    else:
        return s[:k]

n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()

dp = [[None] * (k + 1) for _ in range(n + 1)]

for i in range(k + 1):
    if i > n:
        dp[0][i] = lex_smallest_string(s, k - i)
    else:
        dp[0][i] = s

for i in range(1, n + 1):
    for j in range(k + 1):
        if j <= i:
            dp[i][j] = dp[i-1][j]
        elif j > n:
            dp[i][j] = min(dp[i-1][j], lex_smallest_string(s[:i], k - j))
        else:
            dp[i][j] = min(dp[i-1][j], s[i-1:j])

print(dp[n][k])
