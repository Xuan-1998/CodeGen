from bisect import bisect_left
speed_diffs = []

def max_length(initial_speed, final_speed, max_allowed_change):
    global speed_diffs

    for i in range(1, 101):  # Try speeds from 1 to 100 meters per second
        current_speed = initial_speed + (final_speed - initial_speed) * i / 100
        if abs(current_speed - initial_speed) <= max_allowed_change and \
           abs(current_speed - final_speed) <= max_allowed_change:
            speed_diffs.append((current_speed, 0))  # Add to the list of possible speeds

    return max(sum(1 for j in range(len(speed_diffs) - 1):
                     if abs(speed_diffs[j][0] - speed_diffs[j+1][0]) <=
                    max_allowed_change), default=0)

initial_speed = int(input())
final_speed = int(input())
max_allowed_change = int(input())

print(max_length(initial_speed, final_speed, max_allowed_change))
