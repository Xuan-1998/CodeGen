import sys

def max_path_segment_length():
    initial_speed, final_speed, time, max_change = map(int, input().split())
    dp = [[-1] * (max_change + 1) for _ in range(time + 1)]

    # Base case: The maximum possible length at the first second is 0
    dp[0][0] = 0

    # Iterate over seconds
    for t in range(1, time + 1):
        for mc in range(max_change + 1):
            if t == 1:
                # If it's the first second, only consider the initial speed
                dp[t][mc] = (initial_speed <= final_speed and min(final_speed - initial_speed, max_change)) or -1
            else:
                # Calculate the maximum possible length considering the current speed and remaining distance to travel
                if mc == 0:
                    # If there's no allowed change in speed, consider constant speed
                    dp[t][mc] = dp[t - 1][mc] + min(final_speed - initial_speed, max_change)
                else:
                    # Calculate the maximum possible length for this second considering the allowed change in speed
                    if initial_speed <= final_speed and mc <= min(final_speed - initial_speed, max_change):
                        dp[t][mc] = dp[t - 1][mc - 1] + min(final_speed - initial_speed, max_change)
                    else:
                        dp[t][mc] = -1

    # Return the result
    return dp[time][max_change]

print(max_path_segment_length())
