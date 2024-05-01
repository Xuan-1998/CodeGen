def checkAB(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    def is_valid(i, j):
        if i > j:
            return False
        if s[i:j+1] == 'AB' or s[i:j+1] == 'BA':
            return True
        return False

    for i in range(n):
        dp[i][i] = is_valid(i, i)
        if i < n - 1 and is_valid(i + 1, i + 2):
            dp[i][i + 2] = True

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i:j+1].startswith('A') and s[i+1:j].endswith('B'):
                dp[i][j] = is_valid(i, j)
            elif s[i:j+1].startswith('B') and s[i].endswith('A'):
                dp[i][j] = is_valid(i, j)

    return dp[0][n-1]

s = input()
print("YES" if checkAB(s) else "NO")
