import sys

def max_path_length():
    # Read input from stdin
    initial_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    # Create a 2D array to store intermediate results
    dp = [[0] * (max_change + 1) for _ in range(time + 1)]

    # Initialize the first row and column with base cases
    dp[0][0] = 0
    for i in range(1, time + 1):
        dp[i][0] = initial_speed * i

    # Fill up the rest of the table using dynamic programming
    for i in range(1, time + 1):
        for j in range(1, min(i, max_change) + 1):
            if i == 1:
                dp[i][j] = min(final_speed - initial_speed, j)
            else:
                # Update the maximum possible length based on current speed and remaining distance
                dp[i][j] = max(dp[i-1][j-1] + (i * min(initial_speed, final_speed)), dp[i-1][j])

    # Return the maximum possible length of the path segment
    return dp[time][max_change]

print(max_path_length())
