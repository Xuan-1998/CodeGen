def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = True

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl
            if s[i] == s[j]:
                if cl == 2:
                    dp[i][j] = True
                elif dp[i + 1][j - 1]:
                    dp[i][j] = True

    cuts = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1

    return cuts

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
