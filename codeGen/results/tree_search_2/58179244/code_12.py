from collections import defaultdict

def min_recolors(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    prev_colors = defaultdict(int)

    def recolor(i, p):
        if i > 0:
            c = s[i - 1]
            prev_colors[c] += 1
            if i > 1 and c == s[i - 2]:
                return False
            for j in range(p + 1):
                if prev_colors[s[j]] < 2 and dp[i - 1][j]:
                    return True
        return p == 0

    for i in range(1, n + 1):
        c = s[i - 1]
        prev_colors[c] += 1
        for j in range(n + 1):
            if recolor(i, j):
                dp[i][j] = True
            else:
                dp[i][j] = False

    r = n
    t = s[:]

    while not dp[n - 1][r]:
        r -= 1
        for i in range(n):
            c = s[i]
            if prev_colors[c] == 2 and i < n - 1:
                t[i] = 'R' if c != 'R' else 'G' if c != 'G' else 'B'
    return r, ''.join(t)
