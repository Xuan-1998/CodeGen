def max_path_length(initial_speed, final_speed, time, allowed_change):
    memo = {}

    def dp(speed, remaining_time):
        if (speed, remaining_time) in memo:
            return memo[(speed, remaining_time)]

        if speed == final_speed and remaining_time == 0:
            return 0

        max_length = 0
        for new_speed in [speed - allowed_change, speed, speed + allowed_change]:
            if new_speed >= initial_speed and new_speed <= final_speed:
                length = dp(new_speed, remaining_time - 1)
                max_length = max(max_length, length)

        memo[(speed, remaining_time)] = max_length
        return max_length

    return dp(initial_speed, time)

# Example input
initial_speed, final_speed, time, allowed_change = map(int, input().split())
print(max_path_length(initial_speed, final_speed, time, allowed_change))
