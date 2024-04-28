def max_path_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dp(t, c):
        if (t, c) in memo:
            return memo[(t, c)]

        if t == 0:
            return 0

        speed = initial_speed + (final_speed - initial_speed) * t / time
        length = (speed ** 2) * t
        max_len = dp(t-1, min(max_change, abs(final_speed - speed)))
        memo[(t, c)] = max(len, max_len)
        return memo[(t, c)]

    return int(dp(time, max_change))
