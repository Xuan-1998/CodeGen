def max_path_length(initial_speed, final_speed, travel_time, speed_diff):
    memo = {}

    def dfs(current_speed, time_remaining, prev_speed_diff):
        if (current_speed, time_remaining) in memo:
            return memo[(current_speed, time_remaining)]
        
        if time_remaining == 0:
            return 0
        
        max_length = 0
        for speed in range(max(initial_speed, current_speed), min(final_speed, current_speed + speed_diff) + 1):
            prev_speed = current_speed - (speed - current_speed).abs() // speed_diff * speed_diff
            if abs(speed - prev_speed) <= speed_diff:
                length = dfs(prev_speed, time_remaining - 1, speed_diff)
                max_length = max(max_length, length + travel_time - time_remaining)
        
        memo[(current_speed, time_remaining)] = max_length
        return max_length
    
    return dfs(initial_speed, travel_time, 0)

# Example usage:
initial_speed = int(input())  # Input: Initial speed of the car
final_speed = int(input())   # Input: Final speed of the car
travel_time = int(input())  # Input: Time it takes to travel the distance
speed_diff = int(input())    # Input: Maximum allowed change in speed

max_length = max_path_length(initial_speed, final_speed, travel_time, speed_diff)
print(max_length)  # Output: The maximum possible length of the path segment
