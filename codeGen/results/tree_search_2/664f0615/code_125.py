def max_distance(initial_speed, final_speed, time, max_change):
    # Initialize the memoization table with zeros
    memo = [0] * (time + 1)

    # The maximum distance at the first second is just the initial speed
    memo[0] = initial_speed

    for i in range(1, time + 1):
        # Calculate the maximum allowed change from previous speed
        max_allowed_change = min(max_change, final_speed - memo[i - 1])

        # The maximum distance at this second is either:
        #   the maximum distance at the previous second with the same speed
        #   or the initial speed plus the time it takes to travel half the remaining distance
        if i == 1:
            max_distance_at_this_second = min(memo[i - 1] + (i * 2), initial_speed)
        else:
            max_distance_at_this_second = min(memo[i - 1] + (i * 2) + max_allowed_change, initial_speed)

        # Update the memoization table
        memo[i] = max_distance_at_this_second

    return memo[time]
