def is_scrambled(s1, s2):
    m = len(s1)
    dp = [[False] * (m + 1) for _ in range(m + 1)]

    def dfs(i, j):
        if i == m:
            return j == m
        if dp[i][j]:
            return True

        if s1[i] != s2[j]:
            return False

        dp[i][j] = True

        # If the characters match, we can either swap them or not
        for k in range(m):
            if (k < i and dfs(i - 1, j - 1) and 
                (s1[:i].count(s1[i]) == s2[:j].count(s2[j]))):
                return True

        dp[i][j] = False
        return False

    return dfs(m, m)

# Example usage:
s1 = input()
s2 = input()

if is_scrambled(s1, s2):
    print(True)
else:
    print(False)
