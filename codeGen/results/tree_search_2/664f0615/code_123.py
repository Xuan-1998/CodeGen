def calculate_max_distance(initial_speed, final_speed, time, max_allowed_change):
    memo = {}

    def dfs(current_speed, remaining_time):
        if (current_speed, remaining_time) in memo:
            return memo[(current_speed, remaining_time)]
        if current_speed == final_speed and remaining_time == 0:
            return 0
        if remaining_time == 0:
            return float('inf')

        max_distance = 0
        for i in range(max(1, initial_speed - max_allowed_change), min(final_speed + max_allowed_change, initial_speed) + 1):
            distance = (i * time) / current_speed
            if remaining_time > 0 and i < final_speed:
                max_distance = max(max_distance, dfs(i, remaining_time - 1) + distance)
            elif remaining_time == 0 and i == final_speed:
                max_distance = max(max_distance, distance)

        memo[(current_speed, remaining_time)] = max_distance
        return max_distance

    return int(dfs(initial_speed, time))
