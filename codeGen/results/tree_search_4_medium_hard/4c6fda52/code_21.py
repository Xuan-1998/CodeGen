from sys import stdin

def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if s[i - 1] == 'R' and (j % 3 == 0 or j % 3 == 2):
                dp[i][j] = dp[i - 1][j]
            elif s[i - 1] == 'G' and (j % 3 == 1 or j % 3 == 0):
                dp[i][j] = dp[i - 1][j]
            elif s[i - 1] == 'B' and (j % 3 == 2 or j % 3 == 1):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[n][k]

if __name__ == "__main__":
    t = int(stdin.readline())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        s = stdin.readline().strip()
        print(min_changes(s, k))
