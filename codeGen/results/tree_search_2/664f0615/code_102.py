# Define the limits for the inputs
INITIAL_SPEED = 1
FINAL_SPEED = 100
TIME = 2
MAX_CHANGE = 10

dp = [[0] * (MAX_CHANGE + 1) for _ in range(TIME + 1)]

def solve(initial_speed, final_speed, time, max_change):
    # Initialize the base cases
    dp[0][0] = initial_speed
    dp[time][max_change] = final_speed

    for t in range(1, time + 1):
        for c in range(max_change + 1):
            if t == 1:
                dp[t][c] = min(final_speed, initial_speed + c)
            else:
                # Calculate the maximum possible length at each second
                for prev_c in range(max_change + 1):
                    dp[t][c] = max(dp[t][c], dp[t-1][prev_c] + min(final_speed, initial_speed + c - prev_c))

    return dp[time][max_change]

# Read the input from stdin
initial_speed, final_speed, time, max_change = map(int, input().split())

# Print the result to stdout
print(solve(initial_speed, final_speed, time, max_change))
