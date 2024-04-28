def maximum_path_length():
    init_speed, final_speed = map(int, input().split())
    time_elapsed, max_allowed_diff = map(int, input().split())

    dp = [[0] * (max_allowed_diff + 1) for _ in range(time_elapsed + 1)]

    dp[1][init_speed - final_speed] = 1

    for t in range(2, time_elapsed + 1):
        for diff in range(max_allowed_diff + 1):
            if diff >= abs(final_speed - init_speed):
                dp[t][diff] = min(dp[t-1][max(0, diff - max_allowed_diff)] + (t * (init_speed + final_speed) // 2), t)
            else:
                dp[t][diff] = dp[t-1][diff]

    return dp[time_elapsed][max_allowed_diff]
