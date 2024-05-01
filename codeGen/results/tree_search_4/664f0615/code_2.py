def max_path_segment_length():
    initial_speed, final_speed, time, max_allowed_change_in_speed = [int(x) for x in input().split()]
    dp = [[0] * (max_speed+1) for _ in range(time+1)]

    # Base cases
    dp[0][initial_speed] = 0
    dp[time][final_speed] = 0

    for t in range(1, time+1):
        for v in range(max_speed+1):
            for k in range(max_allowed_change_in_speed+1):
                if abs(v-k) <= max_allowed_change_in_speed:
                    dp[t][v] = max(dp[t-1][v-k]+k, dp[t][v])

    return dp[time][final_speed]

print(max_path_segment_length())
