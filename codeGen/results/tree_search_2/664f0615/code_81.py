def max_path_length(initial_speed, final_speed, time, max_change):
    # Initialize the memoization dictionary
    memo = {(i, 0) for i in range(initial_speed, final_speed + 1)}

    def dp(state):
        speed, t = state

        if t == time:
            return 0

        if (speed - max_change, t + 1) in memo:
            next_state = (speed - max_change, t + 1)
        elif (speed + max_change, t + 1) in memo:
            next_state = (speed + max_change, t + 1)
        else:
            return 0

        # Calculate the maximum possible path length for the next state
        return dp(next_state)

    # Start with the initial state and calculate the maximum possible path length
    result = dp((initial_speed, 0))

    return result
