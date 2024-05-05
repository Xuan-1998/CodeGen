def total_brightness(n, c, queries):
    dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(c+1)]
    
    for i in range(1, n+1):
        x, y, s = [int(x) for x in input().split()]
        
        # Update the DP table based on the star's initial brightness and position
        dp[s][x][y] += s
    
    total_brightnesses = []
    
    for _ in range(q):
        t, x1, y1, x2, y2 = [int(x) for x in input().split()]
        
        # Calculate the total brightness for the given rectangular view
        total_brightness = 0
        
        for s in range(c+1):
            for x in range(x1-1, x2+1):
                for y in range(y1-1, y2+1):
                    total_brightness += dp[s][x][y]
        
        total_brightnesses.append(total_brightness)
    
    return '\n'.join(map(str, total_brightnesses))
