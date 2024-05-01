def max_path_length(initial_speed, final_speed, time_taken, max_change):
    def recursive_max_path_length(current_speeds, time_left):
        if time_left == 0 or len(current_speeds) == 1:
            return sum(current_speeds)
        
        max_length = 0
        for i in range(len(current_speeds)):
            next_speeds = [speed for speed in current_speeds[:i] + [current_speeds[i]] + current_speeds[i+1:]]
            if all(abs(speed - next_speed) <= max_change for speed, next_speed in zip(next_speeds[:-1], next_speeds[1:])):
                length = recursive_max_path_length(next_speeds, time_left-1)
                if length > max_length:
                    max_length = length
        
        return max_length
    
    # Initialize the state
    current_speeds = [initial_speed]
    for _ in range(time_taken-2):
        current_speeds.append(min(final_speed, max(current_speeds[-1] + max_change, initial_speed)))
    current_speeds.append(final_speed)
    
    return recursive_max_path_length(current_speeds, time_taken)

# Example input
initial_speed = 10
final_speed = 20
time_taken = 5
max_change = 3

print(max_path_length(initial_speed, final_speed, time_taken, max_change))
