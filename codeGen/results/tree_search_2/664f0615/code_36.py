import sys

def max_path_segment():
    initial_speed, final_speed, time, max_change = map(int, input().split())
    dp = {}
    
    for i in range(time):
        if i == 0:
            for speed in range(initial_speed, final_speed + 1):
                dp[(i, speed)] = min(i * (speed - initial_speed), sys.maxsize)
        elif i == time - 1:
            for speed in range(final_speed, initial_speed - 1, -1):
                dp[(i, speed)] = min(dp[(i-1, speed-1)], max_change) + 1
        else:
            for speed in range(initial_speed, final_speed + 1):
                if abs(speed - dp.get((i-1, speed), initial_speed)) <= max_change:
                    dp[(i, speed)] = dp[(i-1, speed)] + 1
    
    return max(dp.values())

print(max_path_segment())
