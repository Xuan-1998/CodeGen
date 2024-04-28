def min_rec_colors():
    n = int(input())
    colors = input()
    
    # Initialize a 3D DP array dp[i][c] where i is the index and c is the color (0: red, 1: green, 2: blue)
    dp = [[float('inf')] * 3 for _ in range(n+1)]
    
    # Base case: no recolors needed for an empty garland
    dp[0][0] = dp[0][1] = dp[0][2] = 0
    
    for i in range(1, n+1):
        if colors[i-1] == 'R':  # The current lamp is red
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + 1
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + 1
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + 1
        elif colors[i-1] == 'G':  # The current lamp is green
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + 1
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + 1
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + 1
        elif colors[i-1] == 'B':  # The current lamp is blue
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + 1
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + 1
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + 1
    
    # The minimum number of recolors is stored in the last row of the DP array
    r = min(dp[n])
    
    # Construct a diverse garland with the minimum number of recolors
    t = ''
    for i in range(n):
        if colors[i] == 'R':
            if dp[i+1][0] <= min(dp[i+1][1], dp[i+1][2]):
                t += 'G' if dp[i+1][1] < dp[i+1][2] else 'B'
            elif dp[i+1][1] <= min(dp[i+1][0], dp[i+1][2]):
                t += 'R'
            else:
                t += 'B'
        elif colors[i] == 'G':
            if dp[i+1][0] <= min(dp[i+1][1], dp[i+1][2]):
                t += 'B' if dp[i+1][2] < dp[i+1][0] else 'R'
            elif dp[i+1][1] <= min(dp[i+1][0], dp[i+1][2]):
                t += 'G'
            else:
                t += 'R'
        elif colors[i] == 'B':
            if dp[i+1][0] <= min(dp[i+1][1], dp[i+1][2]):
                t += 'R' if dp[i+1][0] < dp[i+1][1] else 'G'
            elif dp[i+1][1] <= min(dp[i+1][0], dp[i+1][2]):
                t += 'B'
            else:
                t += 'G'
    
    print(r)
    print(t)

min_rec_colors()
