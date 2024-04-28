def max_path_segment_speeds(initial_speed, final_speed, time, delta_speed):
    memo = {}

    def dp(current_speed, current_time):
        if (current_speed, current_time) in memo:
            return memo[(current_speed, current_time)]

        if current_time == 0 or current_speed == initial_speed and current_time == 1:
            return 0

        max_length = 0
        for next_speed in range(max(1, current_speed - delta_speed), min(final_speed + delta_speed, current_speed + delta_speed)):
            length = dp(next_speed, current_time - 1) + abs(current_speed - next_speed)
            max_length = max(max_length, length)

        memo[(current_speed, current_time)] = max_length
        return max_length

    return dp(initial_speed, time)


# Read input from stdin
initial_speed, final_speed, time, delta_speed = [int(x) for x in input().split()]

print(max_path_segment_speeds(initial_speed, final_speed, time, delta_speed))
