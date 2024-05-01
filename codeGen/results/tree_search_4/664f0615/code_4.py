def max_length(initial_speed, final_speed, time, delta):
    dp = [[-float('inf')] * (final_speed - initial_speed + 1) for _ in range(time + 1)]
    
    for i in range(initial_speed, final_speed + 1):
        dp[0][i - initial_speed] = 0

    for t in range(1, time + 1):
        for s in range(initial_speed, final_speed + 1):
            if s <= initial_speed:
                max_length_here = 0
            elif s >= final_speed:
                max_length_here = 0
            else:
                max_length_here = (s - initial_speed) * (t - 1)
            for i in range(max(1, s - delta), min(final_speed + 1, s + delta)):
                max_length_here = max(max_length_here, dp[t - 1][i - initial_speed] + |i - s| * (s <= initial_speed && s <= final_speed))
            dp[t][s - initial_speed] = max_length_here

    return dp[time][final_speed - initial_speed]
