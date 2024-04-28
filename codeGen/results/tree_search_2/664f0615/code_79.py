def max_path_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dp(speed):
        if speed in memo:
            return memo[speed]
        if speed == initial_speed:
            result = 0
        elif speed == final_speed:
            result = time
        else:
            min_time = float('inf')
            for i in range(initial_speed, final_speed + 1):
                if abs(i - speed) <= max_change:
                    time_left = time - (speed - initial_speed)
                    if time_left > 0:
                        min_time = min(min_time, dp(i) + time_left)
            result = min_time
        memo[speed] = result
        return result

    return dp(final_speed)

# Example input and output
initial_speed = int(input())
final_speed = int(input())
time = int(input())
max_change = int(input())

print(max_path_length(initial_speed, final_speed, time, max_change))
