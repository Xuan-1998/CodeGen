def color_text(t, s):
    n = len(s)
    m = len(t)
    dp = [[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if t[i:i+n] == s[j]:
                dp[i][j] = 1 + dp[max(0, i-1)][max(j-1, 0)] if max(i, j) > 0 else 1
            else:
                dp[i][j] = dp[max(0, i-1)][j]
    
    min_steps = float('inf')
    used_strings = []
    for i in range(m):
        for j in range(n):
            if t[i:i+n] == s[j]:
                if dp[i][j] < min_steps:
                    min_steps = dp[i][j]
                    used_strings = [(i, j)]
                elif dp[i][j] == min_steps:
                    used_strings.append((i, j))
    
    return -1 if not used_strings else (min_steps, *zip(*used_strings))
