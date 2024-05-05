def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(i, n + 1):
            if s[i:j+1] == s[i:j+1][::-1]:
                dp[i][j] = True

    cuts = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            if not dp[i][j]:
                cuts += 1

    return cuts

n = int(input())
s = input()
print(min_cuts(s))
