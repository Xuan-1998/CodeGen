def max_path_length():
    # Read input from stdin
    initial_speed, final_speed, time, max_change = map(int, input().split())
    
    # Initialize a table to store the maximum possible lengths for each state
    dp = [[0] * (max_change + 1) for _ in range(time + 1)]
    
    # Base case: The maximum length when the time is 0 is 0
    for i in range(max_change + 1):
        dp[0][i] = 0
    
    # Fill up the table using dynamic programming
    for t in range(1, time + 1):
        for mc in range(1, max_change + 1):
            if t == 1:
                dp[t][mc] = initial_speed * t
            elif t == time:
                dp[t][mc] = final_speed * t
            else:
                # Calculate the maximum possible length considering the current speed and change
                for prev_mc in range(max_change + 1):
                    if abs(initial_speed - final_speed) > mc:
                        continue
                    dp[t][mc] = max(dp[t][mc], dp[t-1][prev_mc] + min(initial_speed, final_speed) * t)
    
    # Return the maximum possible length when the time is equal to the given time and the change is equal to the given maximum change
    return dp[time][max_change]

print(max_path_length())
