import sys

def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = True

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i > 0 or dp[i + 1][j - 1]):
                dp[i][j] = True

    cuts = 0
    for i in range(n - 1):
        if not dp[0][i]:
            cuts += 1

    return cuts

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
