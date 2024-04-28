import sys

dp = {}

def max_length(time, max_change):
    if (time, max_change) in dp:
        return dp[(time, max_change)]
    
    if time == 1:
        return min((0, initial_speed), (final_speed, 0))
    
    if max_change < 0:
        return -float('inf')
    
    if time % 2 == 0:
        speed = (initial_speed + final_speed) // 2
    else:
        if time % 2 == 1 and max_change > initial_speed:
            speed = initial_speed
        elif time % 2 == 1 and max_change < final_speed - initial_speed:
            speed = min(final_speed, initial_speed + max_change)
        else:
            speed = (initial_speed + final_speed) // 2
    
    if speed <= 0 or speed >= max_change:
        return 0
    dp[(time, max_change)] = 1 + max_length(time - 1, abs(speed - initial_speed))
    return dp[(time, max_change)]

initial_speed, final_speed, time, max_change = map(int, sys.stdin.read().split())
print(max_length(time, max_change))
