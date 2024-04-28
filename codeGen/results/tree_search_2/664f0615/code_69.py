def max_path_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dp(time_left, current_speed):
        if (time_left, current_speed) in memo:
            return memo[(time_left, current_speed)]
        
        if time_left == 0:
            return 0
        
        if current_speed < initial_speed:
            speed_up = min(initial_speed, current_speed + max_change)
            path_length = dp(time_left - 1, speed_up) + abs(speed_up - current_speed)
        elif current_speed > final_speed:
            slow_down = max(final_speed, current_speed - max_change)
            path_length = dp(time_left - 1, slow_down) + abs(slow_down - current_speed)
        else:
            path_length = dp(time_left - 1, current_speed) + time_left
        
        memo[(time_left, current_speed)] = path_length
        return path_length
    
    return max(dp(time, initial_speed), key=lambda x: x)

initial_speed, final_speed, time, max_change = map(int, input().split())
print(max_path_length(initial_speed, final_speed, time, max_change))
