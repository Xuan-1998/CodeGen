def diverse_garland(n, s):
    dp = [[0] * 3 for _ in range(n+1)]
    
    colors = {'R': 0, 'G': 1, 'B': 2}
    color_map = {0: 'R', 1: 'G', 2: 'B'}
    
    for i in range(1, n+1):
        if s[i-1] == 'R':
            dp[i][colors['R']] += 1
            dp[i][colors['G']] += 1
        elif s[i-1] == 'G':
            dp[i][colors['G']] += 1
            dp[i][colors['B']] += 1
        else:
            dp[i][colors['B']] += 1
            dp[i][colors['R']] += 1
    
    min_rec = float('inf')
    rec_garland = ''
    
    for i in range(1, n+1):
        for j in range(3):
            if dp[i][j] == i:
                min_rec = min(min_rec, i)
                rec_garland = ''.join([color_map[k] if k == 0 else s[k-1] for k in range(i)])
    
    return min_rec, rec_garland
