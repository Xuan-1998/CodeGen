def max_distance_speed(initial_speed, final_speed, time, max_change):
    # Initialize memoization dictionary with initial state
    memo = {(1, 0): 0}

    def dfs(speed, second):
        if (speed, second) in memo:
            return memo[(speed, second)]
        
        if speed == final_speed and second == time:
            return int((final_speed - initial_speed) * time + initial_speed)
        
        next_speed = min(final_speed, max(initial_speed, speed + max_change))
        memo[(next_speed, second+1)] = dfs(next_speed, second+1)
        memo[(speed, second)] = int((second-1)*initial_speed + 0.5) if second > 1 else 0
        return max(memo[(speed, second)], memo[(next_speed, second+1)])

    return dfs(initial_speed, 1)

# Read input from stdin
initial_speed, final_speed, time, max_change = map(int, input().split())

# Calculate and print the maximum possible length of the path segment
print(max_distance_speed(initial_speed, final_speed, time, max_change))
