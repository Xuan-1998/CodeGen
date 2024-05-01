def max_path_length(initial_speed, final_speed, time, max_change):
    dp = [[0] * (time + 1) for _ in range(final_speed - initial_speed + 1)]

    for j in range(time + 1):
        if j == 0:
            continue

        for i in range(initial_speed, final_speed + 1):
            if j == 1:
                dp[i - initial_speed][j] = (i * time) // (final_speed - initial_speed)
            else:
                max_length = 0
                for k in range(max(-max_change, 0), min(max_change + 1, j)):
                    speed_segment = [initial_speed]
                    if i != initial_speed:
                        speed_segment.append(i)
                    if final_speed != i:
                        speed_segment.append(final_speed)
                    speed_segment.sort()
                    last_speed = 0
                    length = 0
                    for s in speed_segment:
                        if s > last_speed + max_change and k > 0:
                            break
                        last_speed = s
                        length += j - (speed_segment.index(s) + 1)
                    max_length = max(max_length, dp[i - initial_speed - 1][j - (speed_segment.index(i) + 1)] + length)
                dp[i - initial_speed][j] = max_length

    return max(dp)

initial_speed = int(input())
final_speed = int(input())
time = int(input())
max_change = int(input())

print(max_path_length(initial_speed, final_speed, time, max_change))
