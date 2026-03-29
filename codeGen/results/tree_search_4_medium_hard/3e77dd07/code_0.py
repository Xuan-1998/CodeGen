def isScramble(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)

    def dfs(i: int, j: int) -> bool:
        if i == 0:
            return j == 0
        if dp[i][j]:
            return True

        if s1[i - 1] != s2[j - 1]:
            return False

        for x in range(1, n):
            for y in range(1, m):
                if (dfs(i - x, j - y) and
                        dfs(i - x, j - (m - y)) and
                        dfs(x, j - y)):
                    dp[i][j] = True
                    return True

        return False

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    return dfs(n, m)
