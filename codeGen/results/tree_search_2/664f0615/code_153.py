def solve():
    initial_speed, final_speed, time, max_change = [int(i) for i in input().split()]
    
    dp = [[0] * (max_change + 1) for _ in range(time + 1)]
    
    for i in range(1, time + 1):
        speed = min(initial_speed + i * (final_speed - initial_speed) // (time), final_speed)
        
        for j in range(min(max_change + 1, i), 0, -1):
            dp[i][j] = max(dp[i-1][j-1] + abs(speed - dp[i-1][j-1]), dp[i][j])
    
    return int(max([dp[i][max_change] for i in range(time)]))
