def max_path_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dp(time, speed):
        if (time, speed) in memo:
            return memo[(time, speed)]
        
        if time == 0:
            return 0
        
        if speed < initial_speed or speed > final_speed:
            return -float('inf')

        max_len = 0
        for next_speed in range(initial_speed, final_speed + 1):
            if abs(next_speed - speed) <= max_change:
                max_len = max(max_len, dp(time - 1, next_speed))
        
        memo[(time, speed)] = max_len + (speed * time)
        return memo[(time, speed)]

    return dp(time, initial_speed)

# Example input
initial_speed, final_speed, time, max_change = map(int, input().split())

print(max_path_length(initial_speed, final_speed, time, max_change))
