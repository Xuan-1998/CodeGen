def max_path_length(initial_speed, final_speed, time, speed_change):
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

    for t in range(1, time + 1):
        for s in range(initial_speed, final_speed + 1):
            if t == 1:
                # initial state
                dp[t][s] = min(s - initial_speed, final_speed - s) * (initial_speed <= s <= final_speed)
            else:
                # transition states
                max_length = 0
                for prev_s in range(max(0, s - speed_change), min(final_speed + 1, s + speed_change)):
                    max_length = max(max_length, dp[t-1][prev_s] + abs(s - prev_s))
                dp[t][s] = max_length

    return dp[time][final_speed]
