import sys

def solve():
    # Read input from standard input
    initial_speed, final_speed, time, max_change = map(int, input().split())
    
    # Create a 2D array to store DP states
    dp = [[0] * (max(initial_speed, final_speed) + 1) for _ in range(time + 1)]

    # Initialize the base case: 1 meter is always possible with any speed
    for j in range(max(initial_speed, final_speed) + 1):
        dp[0][j] = 1

    # Fill up the DP table
    for i in range(1, time + 1):
        for j in range(min(final_speed, initial_speed), -1, -1):
            if abs(j - initial_speed) <= max_change:
                dp[i][j] = min(dp[i-1][j], dp[i-1][initial_speed] + (j * i))
            else:
                break
        for j in range(min(final_speed, initial_speed), -1, -1):
            if abs(j - final_speed) <= max_change:
                dp[i][j] = min(dp[i][j], dp[i-1][final_speed] + (j * i))
            else:
                break

    # Find the maximum possible length
    max_length = 0
    for j in range(min(final_speed, initial_speed), -1, -1):
        if abs(j - final_speed) <= max_change and dp[time][j] > max_length:
            max_length = dp[time][j]

    # Print the result to standard output
    print(max_length)

# Run the solve function
solve()
