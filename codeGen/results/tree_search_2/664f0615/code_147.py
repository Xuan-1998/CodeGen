def max_path_length(initial_speed, final_speed, time, max_change):
    # Create a 2D table to store intermediate results
    dp = [[0] * (max_change + 1) for _ in range(final_speed - initial_speed + 1)]

    # Initialize the base case: if all seconds are exhausted or the maximum allowed change is reached
    for i in range(final_speed - initial_speed, 0, -1):
        if time == 0:
            dp[i][max_change] = max_path_length_at_speed(i + initial_speed)
        elif i <= max_change:
            # If we reach this point, it means the maximum allowed change is reached
            # So, we should stop increasing the speed
            dp[i][max_change] = time * (i + initial_speed) / 2
        else:
            # Calculate the maximum length for the current state and transition to next states
            for j in range(max_change + 1):
                if i - j > max_change:
                    dp[i][j] = min(dp[i-j][max_change], time * (i + initial_speed) / 2)
                else:
                    dp[i][j] = dp[i-j][j]

    return int(dp[final_speed - initial_speed][max_change])

def max_path_length_at_speed(speed):
    # Calculate the maximum path length for a given speed
    return speed

if __name__ == "__main__":
    initial_speed, final_speed, time, max_change = map(int, input().split())
    print(max_path_length(initial_speed, final_speed, time, max_change))
