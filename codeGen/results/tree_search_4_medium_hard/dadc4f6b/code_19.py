def calculate_brightness(n, c, q):
    dp = [[0] * 101 for _ in range(101)]
    
    for i in range(n):
        x1, y1, s_i = [int(x) for x in input().split()]
        
        # Calculate the initial brightness of this star
        brightness = min(c, s_i)
        
        # Update the memoized table for all stars within the view at time 0
        for j in range(100, -1, -1):
            if y1 > j:
                break
            for k in range(100, -1, -1):
                if x1 > k:
                    break
                dp[j][k] += brightness
                
    total_brightness = 0
    for _ in range(q):
        t, x1, y1, x2, y2 = [int(x) for x in input().split()]
        
        # Update the memoized table based on the new line segments added to the view
        for j in range(y1 - 1, -1, -1):
            for k in range(x1 - 1, -1, -1):
                if dp[j][k] > c:
                    total_brightness += (min(c, dp[j][k]) * ((x2 - x1 + 1) * (y2 - y1 + 1)))
        
        print(total_brightness)
