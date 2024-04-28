def max_path_length(initial_speed, final_speed, time, speed_diff):
    dp = {(0, 0): 0}  # base case: initial speed at time 0

    for t in range(1, time + 1):
        for s in range(min(initial_speed, final_speed), max(initial_speed, final_speed) + 1):
            if abs(s - initial_speed) <= speed_diff:
                dp[(s, t)] = dp.get((initial_speed, t - 1), 0) + s
            elif abs(s - final_speed) <= speed_diff:
                dp[(s, t)] = dp.get((final_speed, time - t), 0) + s
            else:  # adjust speed within the allowed range
                for prev_s in range(min(initial_speed, final_speed), max(initial_speed, final_speed) + 1):
                    if abs(prev_s - initial_speed) <= speed_diff and abs(s - prev_s) <= speed_diff:
                        dp[(s, t)] = dp.get((prev_s, t - 1), 0) + s
                    elif abs(prev_s - final_speed) <= speed_diff and abs(s - prev_s) <= speed_diff:
                        dp[(s, t)] = dp.get((final_speed, time - t), 0) + s

    return max(dp.values())

# Example usage:
initial_speed, final_speed, time, speed_diff = map(int, input().split())
print(max_path_length(initial_speed, final_speed, time, speed_diff))
