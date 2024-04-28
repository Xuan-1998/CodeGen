def min_recolors_initial_color(s):
    n = len(s)
    dp = [[0, False] for _ in range(n)]
    
    # Base case: first lamp
    if s[0] == 'R':
        dp[0][1] = True
    
    for i in range(1, n):
        prev_color = 0 if s[i-1] == 'R' else (1 if s[i-1] == 'G' else 2)
        dp[i][0] = min((dp[j][0] + (1 if j - i > 0 and dp[j-1][1] != prev_color else 0)) for j in range(i))
    
    return dp[-1][0], [s[i] if not dp[i][1] else ['R', 'G', 'B'][prev_color] for i in range(n)]
