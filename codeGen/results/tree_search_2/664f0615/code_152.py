def max_path_length(initial_speed, final_speed, time_taken, max_change):
    # Initialize a dictionary to store intermediate results using memoization
    memo = {}

    def dfs(seconds_left, current_speed):
        if (seconds_left, current_speed) in memo:
            return memo[(seconds_left, current_speed)]
        
        # Base case: when all seconds are exhausted or the maximum allowed change is reached
        if seconds_left == 0 or abs(current_speed - final_speed) > max_change:
            return 0

        # Calculate the distance traveled at the current speed
        distance = (current_speed * time_taken + time_taken**2 / 2) * seconds_left
        
        # Update the maximum possible length of the path segment
        max_length = max(dfs(seconds_left - 1, initial_speed), 
                          dfs(seconds_left - 1, current_speed - min(max_change, final_speed - current_speed)), 
                          key=lambda x: x[0] + distance)
        
        memo[(seconds_left, current_speed)] = max_length
        return max_length

    # Initialize the maximum possible length of the path segment
    max_length = 0

    # Start from the initial speed and travel the given time
    for _ in range(time_taken):
        max_length = dfs(time_taken, initial_speed)

    return max_length


# Receive input from stdin
initial_speed, final_speed, time_taken, max_change = map(int, input().split())

# Calculate and print the maximum possible length of the path segment
print(max_path_length(initial_speed, final_speed, time_taken, max_change))
