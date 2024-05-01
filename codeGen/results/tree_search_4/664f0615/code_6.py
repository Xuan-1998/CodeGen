def max_path_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dfs(speed_segment, time_left):
        if (speed_segment, time_left) in memo:
            return memo[(speed_segment, time_left)]

        if time_left == 0 or len(speed_segment) == 2:
            return abs(final_speed - initial_speed)

        next_speeds = []
        for i in range(1, len(speed_segment)):
            speed_diff = abs(speed_segment[i] - speed_segment[i-1])
            if speed_diff <= max_change and time_left >= 1:
                next_speeds.append((speed_segment[:i], speed_segment[i:]))
                break

        if not next_speeds:
            return abs(final_speed - initial_speed)

        max_length = float('-inf')
        for segment in next_speeds:
            length = dfs(segment[0] + [segment[1][-1]], time_left - 1)
            max_length = max(max_length, length)

        memo[(speed_segment, time_left)] = max_length
        return max_length

    return dfs([initial_speed], time)
