def isScramble(s1, s2):
    n = len(s1)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i > n or j > n:
            return False
        if dp[i][j]:
            return True
        if s1[i - 1] != s2[j - 1]:
            return False

        for x in range(1, n + 1):
            if dfs(i - x, j) and dfs(i, j - x):
                return True

        dp[i][j] = True
        return True

    return dfs(n, n)

s1 = input()
s2 = input()

if isScramble(s1, s2):
    print(True)
else:
    print(False)
