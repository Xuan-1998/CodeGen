import sys

def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n)]

    prev_color = None
    for i in range(n):
        for j in range(k, -1, -1):  # consider substrings of length k ending at i
            if s[i - j + 1:i + 1] == 'RGB'[j % 3]:  # substring appears in infinite string
                dp[i][k] = min(dp[i][k], dp[i - j][j])
            else:
                prev_color = 'RGB'[j % 3]
        for c in range(k + 1):  # update dp[i][c]
            if s[i - k + 1:i + 1] == 'RGB'[c]:
                dp[i][c] = min(dp[i][c], dp[i - 1][k])
            else:
                prev_color = 'RGB'[c]
        dp[i][0] = sum(1 for c in s[:i + 1] if c != prev_color)

    return dp[n - 1][k]

while True:
    n, k = map(int, sys.stdin.readline().split())
    if not (n and k):
        break
    s = sys.stdin.readline().strip()
    print(min_changes(s, k))
