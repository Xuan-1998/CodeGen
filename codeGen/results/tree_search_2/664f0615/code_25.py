from collections import defaultdict

def max_length_speed_change():
    initial_speed, final_speed, time, max_speed_diff = [int(x) for x in input().split()]
    
    dp = [[0] * (max_speed_diff + 1) for _ in range(time + 1)]
    prev_speeds = defaultdict(int)

    for i in range(1, time + 1):
        prev_speeds[initial_speed] += dp[i - 1][abs(initial_speed - final_speed)] + abs(initial_speed - final_speed)
        if i < time:
            for speed_diff in range(max_speed_diff + 1):
                if abs(prev_speeds.get(speed_diff, 0) - initial_speed) <= max_speed_diff:
                    prev_speeds[speed_diff] = dp[i - 1][speed_diff]
                    if i > 1:
                        prev_speeds[abs(initial_speed - final_speed)] = max(prev_speeds[abs(initial_speed - final_speed)], prev_speeds.get(speed_diff, 0) + abs(initial_speed - final_speed))
                else:
                    prev_speeds[speed_diff] = dp[i - 1][speed_diff]
    
    return prev_speeds[max_speed_diff]

print(max_length_speed_change())
