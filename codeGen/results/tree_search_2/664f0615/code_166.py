import sys

def solve():
    initial_speed, final_speed = map(int, input().split())
    time, max_change_speed = map(int, input().split())

    dp = {(time, 0): 0}
    for t in range(time - 1, -1, -1):
        for d in range(10001):
            if (t, d) not in dp:
                continue
            speed_diff = abs(final_speed - initial_speed)
            for i in range(min(d, time), -1, -1):
                if i > 0 and (i - 1, d - i) in dp:
                    max_length = dp[(i - 1, d - i)] + i * initial_speed
                    speed_diff_new = abs(initial_speed - final_speed)
                    for j in range(min(speed_diff_new, max_change_speed), -1, -1):
                        if (t - i, d - i) not in dp:
                            continue
                        dp[(t - i, d - i)] = max(dp.get((t - i, d - i), 0), max_length + j)
                speed_diff_new = min(speed_diff_new, abs(final_speed - initial_speed))
            dp[(t, d)] = dp.get((t, d), 0)

    return dp.get((0, 10001), 0)


print(solve())
