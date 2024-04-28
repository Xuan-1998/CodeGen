def diverse_garland():
    n = int(input())
    s = input()
    
    dp = [[0]*3 for _ in range(n+1)]
    prev_color = {'R': 'G', 'G': 'B', 'B': 'R'}
    color_count = [0]*3
    
    # Initialize base cases
    for i in range(3):
        dp[1][i] = 1
        color_count[i] += 1
    
    for i in range(2, n+1):
        for j in range(3):
            if (dp[i-1][j] and not prev_color[s[i-1]] == 'R' or 
                dp[i-1][color_count.index(prev_color[s[i-1]])]):
                color_count[j] += 1
                dp[i][j] = 1
            else:
                dp[i][j] = 0
            
    min_recolors = float('inf')
    diverse_garland = ''
    
    for i in range(3):
        if dp[n][i]:
            min_recolors = min(min_recolors, color_count[i])
            diverse_garland = s[:n].replace(s[n-1], str(i+1))
            break
    
    print(min_recolors)
    print(diverse_garland)

diverse_garland()
