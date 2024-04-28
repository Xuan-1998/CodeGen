def max_path_length():
    initial_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    # Initialize a 2D table with (time + 1) rows and (max_change + 1) columns
    dp = [[0] * (max_change + 1) for _ in range(time + 1)]

    # Base case: when all seconds are exhausted or the maximum allowed change is reached
    for i in range(max_change + 1):
        if i > max_change:
            dp[time][i] = time * initial_speed
        elif i == max_change:
            dp[time][i] = time

    # Transition: update the number of seconds left to travel and the maximum allowed change
    for t in range(time - 1, -1, -1):
        for c in range(max_change + 1):
            if c > max_change:
                dp[t][c] = min(dp[t][c], dp[t-1][max_change])
            elif c == max_change:
                dp[t][c] = t
            else:
                dp[t][c] = dp[t-1][min(c, max_change)]

    # The maximum possible length of the path segment is the maximum value in the last row
    return max(dp[-1])

print(max_path_length())
