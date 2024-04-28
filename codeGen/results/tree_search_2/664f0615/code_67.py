def max_path_length():
    # Read input from stdin
    init_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    # Initialize dynamic programming table
    dp = [[0] * (max_time := time + 1) for _ in range(max_speed := max(final_speed, init_speed) + 1)]

    # Base case: the maximum length of a path segment at the initial speed is zero
    for i in range(max_speed + 1):
        dp[i][0] = 0

    # Fill up the dynamic programming table
    for t in range(1, max_time + 1):
        for s in range(max_speed + 1):
            if t == 1:
                dp[s][t] = min(s, final_speed) * max_change
            else:
                for prev_s in range(max_speed + 1):
                    # Calculate the maximum length of a path segment given the current speed and time
                    dp[s][t] = max(dp[s][t], dp[prev_s][t - 1] + min(s, final_speed) * max_change)

    # Print the answer to stdout
    print(max(dp))

max_path_length()
