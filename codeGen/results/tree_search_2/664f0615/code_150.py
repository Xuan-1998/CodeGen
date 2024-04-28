def max_path_length():
    initial_speed, final_speed, time, speed_change = map(int, input().split())
    dp = {(0, 0): 0}

    for seconds in range(1, time + 1):
        for max_speed in range(initial_speed, final_speed + 1):
            if (seconds - 1, max_speed) in dp:
                if abs(max_speed - min(final_speed, initial_speed + speed_change * seconds)) <= speed_change:
                    dp[(seconds, max_speed)] = min(dp.get((seconds - 1, max_speed), float('inf')), seconds * max_speed)
                else:
                    dp[(seconds, max_speed)] = dp.get((seconds - 1, max_speed), 0)

    return max(dp.values())

print(max_path_length())
