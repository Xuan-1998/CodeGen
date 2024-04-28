def max_length_segments():
    initial_speed, final_speed = map(int, input().split())
    time_to_travel, max_speed_diff = map(int, input().split())

    dp = [[0] * (time_to_travel + 1) for _ in range(final_speed + 1)]

    for speed in range(initial_speed, final_speed + 1):
        for time in range(time_to_travel + 1):
            if time == 0:
                continue
            elif time == 1:
                dp[speed][time] = speed * (1 if speed <= initial_speed else -1)
            else:
                max_length = 0
                for prev_speed in range(max(1, speed - max_speed_diff), min(final_speed + 1, speed + 1)):
                    length = dp[prev_speed][time - 1] + abs(prev_speed - speed) * (1 if prev_speed <= initial_speed else -1)
                    max_length = max(max_length, length)
                dp[speed][time] = max_length

    return max([dp[-1][i] for i in range(time_to_travel + 1)])

print(max_length_segments())
