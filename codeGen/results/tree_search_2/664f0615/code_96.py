from functools import lru_cache

@lru_cache(maxsize=None)
def max_length(time, max_change):
    if time == 1:
        return min(v) * 100  # minimum speed in meters per second
    elif time >= len(speeds):
        return (speeds[-1] - speeds[0]) * 100  # final to initial speed change

    # calculate the minimum speed required to reach the final speed within the allowed change
    min_speed = max_length(time - 1, max_change) + max_change
    if min_speed > max_length(time - 2, max_change):
        return (min_speed - speeds[0]) * 100  # adjust the initial speed

    return max_length(time - 1, max_change)

# read input from stdin
initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]

speeds = [initial_speed] + [(final_speed - i * (max_change // (time - 1))) % (max_change // (time - 1)) + initial_speed for i in range(time - 1)] + [final_speed]

print(max_length(time, max_change))
