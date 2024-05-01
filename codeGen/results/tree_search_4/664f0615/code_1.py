def max_path_length():
    # Read input from stdin
    initial_speed, final_speed = map(int, input().split())
    time_range, max_allowed_change_in_speed = map(int, input().split())

    # Initialize memoization dictionary
    dp = {(t, v): 0 for t in range(time_range + 1) for v in range(initial_speed, final_speed + 1)}

    # Fill DP table using transition relationship and memoization
    for t in range(2, time_range + 1):
        for v in range(min(initial_speed, final_speed), max(final_speed, initial_speed)):
            dp[(t, v)] = max(
                dp.get((t - 1, min(v + max_allowed_change_in_speed, final_speed)), 0) +
                (v - min(initial_speed, v)),
                dp.get((t - 1, min(v - max_allowed_change_in_speed, initial_speed)), 0) +
                (v - min(initial_speed, v))
            )

    # Return the maximum possible length
    return dp[(time_range, final_speed)]

print(max_path_length())
