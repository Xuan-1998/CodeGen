def max_length(initial_speed, final_speed, time, max_change):
    memo = {}
    
    def dp(remaining_time, remaining_distance):
        if (remaining_time, remaining_distance) in memo:
            return memo[(remaining_time, remaining_distance)]
        
        if remaining_time == 0 or remaining_distance <= 0:
            return 0
        
        if remaining_distance < time:
            max_speed = min(initial_speed + remaining_time * final_speed / time, final_speed)
            length = (max_speed ** 2) * time - (initial_speed ** 2) * time
            memo[(remaining_time, remaining_distance)] = length
            return length
        
        for speed in range(min(initial_speed + max_change, final_speed), initial_speed - 1, -1):
            if speed > final_speed:
                continue
            
            length = dp(remaining_time - 1, remaining_distance - time)
            memo[(remaining_time, remaining_distance)] = max(length, length + (speed ** 2) * time - (initial_speed ** 2) * time)
            break
        
        return memo[(remaining_time, remaining_distance)]
    
    return dp(time, initial_speed * time)

# Read input from standard input
initial_speed, final_speed, time, max_change = map(int, input().split())
print(max_length(initial_speed, final_speed, time, max_change))
