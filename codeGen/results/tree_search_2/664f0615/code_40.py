def max_length(t, init_speed, allowed_change):
    # Base case: when t is 1, the maximum length is simply the product of init_speed and t
    if t == 1:
        return init_speed * t

    # Initialize a table to store the maximum lengths for each possible time
    dp = [0] * (t + 1)

    # The maximum length at time 0 is 0, since we haven't traveled any distance yet
    dp[0] = 0

    # Fill up the table using dynamic programming
    for i in range(1, t + 1):
        # For each possible speed between init_speed and final_speed, calculate the maximum length
        for j in range(min(init_speed, allowed_change), max(final_speed, init_speed - allowed_change)):
            dp[i] = max(dp[i], j * (i - 1) + dp[i - 1])

    # Return the maximum length at time t
    return dp[t]
