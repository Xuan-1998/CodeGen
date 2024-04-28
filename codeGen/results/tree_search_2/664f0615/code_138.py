def max_path_length(initial_speed, final_speed, time, speed_change_limit):
    memo = {}

    def dfs(remaining_distance, current_speed, time_elapsed):
        if (remaining_distance, current_speed, time_elapsed) in memo:
            return memo[(remaining_distance, current_speed, time_elapsed)]

        if remaining_distance == 0:
            return 0

        max_length = 0
        for new_speed in range(min(final_speed, current_speed + speed_change_limit), max(initial_speed, current_speed - speed_change_limit) + 1):
            length = dfs(remaining_distance - (new_speed * time_elapsed), new_speed, time_elapsed + 1)
            if length > max_length:
                max_length = length

        memo[(remaining_distance, current_speed, time_elapsed)] = max_length
        return max_length

    return dfs(time * initial_speed, initial_speed, 0)

if __name__ == "__main__":
    initial_speed, final_speed, time, speed_change_limit = map(int, input().split())
    print(max_path_length(initial_speed, final_speed, time, speed_change_limit))
