def dp(initial_speed, final_speed, max_change, time):
    memo = {}
    
    def dfs(speed, time_left):
        if (speed, time_left) in memo:
            return memo[(speed, time_left)]
        
        if time_left == 0:
            return 0
        
        if speed < initial_speed or speed > final_speed:
            return dfs(initial_speed if speed < initial_speed else final_speed, time_left - 1)
        
        max_length = 0
        for new_speed in [speed + max_change, speed - max_change]:
            if initial_speed <= new_speed <= final_speed:
                length = time_left * (new_speed - initial_speed) // (final_speed - initial_speed)
                max_length = max(max_length, dfs(new_speed, time_left - 1))
        
        memo[(speed, time_left)] = max_length + time_left
        return memo[(speed, time_left)]
    
    return dfs(initial_speed, time)
