def max_length(initial_speed, final_speed, time_allowed_change):
    dp = {(initial_speed, 0): 0}  # Base case: initial speed at time 0

    for _ in range(time_allowed_change + 1):
        for (speed, time) in list(dp.items()):
            if speed != initial_speed and speed != final_speed:
                next_speeds = [(speed - 1, time + 1), (speed + 1, time + 1)]
                for next_speed, next_time in next_speeds:
                    dp[(next_speed, next_time)] = max(dp.get((next_speed, next_time), 0), speed * time)
            if speed == initial_speed and time < _:
                dp[(speed, time + 1)] = dp.get((speed, time), 0) + speed
            elif speed == final_speed and time < _:
                dp[(speed, time + 1)] = max(dp.get((speed, time), 0), speed * (time + 1))

    return max(dp.values())

# Read input from stdin
initial_speed, _, _, time_allowed_change = [int(x) for x in input().split()]
final_speed, _, _, _ = [int(x) for x in input().split()]

print(max_length(initial_speed, final_speed, time_allowed_change))
